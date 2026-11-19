"""Pre-annotation of zone crops with a large detector run by tiles (ADR 0029).

The pre-annotation model must be stronger than, and different from, the model under evaluation:
a large detector, high resolution, overlapping tiles, low confidence threshold (deleting a wrong
proposal is cheaper than spotting a missed person). Each detection becomes a point at the feet
(bottom-centre of the box), labelled with our classes:

    person + skis      -> skieur          car   -> voiture
    person + snowboard -> snowboardeur    truck -> camion
    person alone       -> pieton          bus   -> bus
    dog / cat / horse  -> animal          (engin_neige: no COCO class, never proposed)

Points that fall in the greyed-out part of a crop (outside the zone) are dropped.

Usage:
    python -m flowview.preannotate data/reference/sessions/A_zones out.json --weights yolo26x.pt
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PERSON, SKIS, SNOWBOARD = 0, 30, 31
OBJECTS = {2: "voiture", 7: "camion", 5: "bus", 16: "animal", 15: "animal", 17: "animal"}
KEEP = {PERSON, SKIS, SNOWBOARD, *OBJECTS}
GREY = (128, 128, 128)


def tiles(width: int, height: int, size: int, overlap: float) -> list[tuple[int, int, int, int]]:
    """Overlapping tiles covering the whole image (the last row/column is aligned on the border)."""
    step = max(1, int(size * (1 - overlap)))

    def starts(n: int) -> list[int]:
        if n <= size:
            return [0]
        s = list(range(0, n - size, step))
        return s + [n - size]

    return [(x, y, min(x + size, width), min(y + size, height)) for y in starts(height) for x in starts(width)]


def iou(a: list[float], b: list[float]) -> float:
    ix = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = ix * iy
    union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    return inter / union if union > 0 else 0.0


def nms(dets: list[dict], thr: float = 0.5) -> list[dict]:
    """Greedy per-class non-maximum suppression, to merge duplicates from overlapping tiles."""
    out: list[dict] = []
    for d in sorted(dets, key=lambda d: -d["conf"]):
        if all(o["cls"] != d["cls"] or iou(o["box"], d["box"]) < thr for o in out):
            out.append(d)
    return out


def classify_people(dets: list[dict]) -> list[dict]:
    """Turn COCO boxes into our classes; equipment boxes only serve to qualify people."""
    gear = [d for d in dets if d["cls"] in (SKIS, SNOWBOARD)]
    out = []
    for d in dets:
        if d["cls"] == PERSON:
            x0, y0, x1, y1 = d["box"]
            h = y1 - y0
            label = "pieton"
            for g in gear:   # equipment touching the lower half of the person
                gx0, gy0, gx1, gy1 = g["box"]
                if gx1 > x0 - 0.2 * h and gx0 < x1 + 0.2 * h and gy1 > y0 + 0.5 * h and gy0 < y1 + 0.3 * h:
                    label = "skieur" if g["cls"] == SKIS else "snowboardeur"
                    break
            out.append({**d, "label": label})
        elif d["cls"] in OBJECTS:
            out.append({**d, "label": OBJECTS[d["cls"]]})
    return out


def is_grey(img, x: float, y: float, tol: int = 6) -> bool:
    px = img.getpixel((min(int(x), img.width - 1), min(int(y), img.height - 1)))
    return all(abs(c - g) <= tol for c, g in zip(px[:3], GREY))


def run(paths: list[Path], weights: str, tile: int, overlap: float, conf: float, device: str) -> dict:
    from PIL import Image
    from ultralytics import YOLO

    model = YOLO(weights)
    result: dict = {"weights": weights, "tile": tile, "overlap": overlap, "conf": conf, "images": {}}
    for i, path in enumerate(paths, 1):
        img = Image.open(path).convert("RGB")
        dets = []
        for x0, y0, x1, y1 in tiles(img.width, img.height, tile, overlap):
            r = model.predict(img.crop((x0, y0, x1, y1)), imgsz=tile, conf=conf, device=device,
                              classes=sorted(KEEP), verbose=False)[0]
            for b, c, k in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist(), r.boxes.cls.tolist()):
                dets.append({"cls": int(k), "conf": float(c), "box": [b[0] + x0, b[1] + y0, b[2] + x0, b[3] + y0]})
        points = []
        for d in classify_people(nms(dets)):
            x0, y0, x1, y1 = d["box"]
            fx, fy = (x0 + x1) / 2, min(y1, img.height - 1)
            if not is_grey(img, fx, fy):
                points.append({"label": d["label"], "x": round(fx, 1), "y": round(fy, 1), "conf": round(d["conf"], 3)})
        result["images"][path.name] = points
        print(f"[{i}/{len(paths)}] {path.name}: {len(points)} points", flush=True)
    return result


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Pre-annotate zone crops with a large tiled detector.")
    ap.add_argument("images_dir")
    ap.add_argument("out")
    ap.add_argument("--weights", default="yolo26x.pt")
    ap.add_argument("--tile", type=int, default=1280)
    ap.add_argument("--overlap", type=float, default=0.25)
    ap.add_argument("--conf", type=float, default=0.20)
    ap.add_argument("--device", default="0")
    a = ap.parse_args(argv[1:])
    paths = sorted(Path(a.images_dir).glob("*.jpg"))
    res = run(paths, a.weights, a.tile, a.overlap, a.conf, a.device)
    Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{sum(len(v) for v in res['images'].values())} points -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
