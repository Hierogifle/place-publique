"""Counting zones: polygons drawn per camera, point-in-zone tests and zone crops.

A zone is where the operator takes a decision (a station, a queue, a terrace). Counts are made
inside zones only (ADR 0028). Polygons are stored in pixels of the reference panorama size and
scaled if an image has another size. A point that falls in two zones belongs to the first one.

Usage (crops of the blind set, outside of the zone greyed out):
    python -m flowview.zones configs/zones_lesarcs.json data/reference/blind_set.csv \
        data/reference/images data/reference/sessions/A_zones [--skip ARC-03]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

Point = tuple[float, float]
GREY = (128, 128, 128)


def load_zones(path: Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))["cameras"]


def scaled(polygon: list[list[float]], ref_size: list[int], size: tuple[int, int]) -> list[Point]:
    sx, sy = size[0] / ref_size[0], size[1] / ref_size[1]
    return [(x * sx, y * sy) for x, y in polygon]


def point_in_polygon(p: Point, poly: list[Point]) -> bool:
    """Ray casting; points exactly on an edge may go either way (irrelevant at pixel scale)."""
    x, y = p
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def zone_of(p: Point, camera: dict, size: tuple[int, int]) -> str | None:
    for z in camera["zones"]:
        if point_in_polygon(p, scaled(z["polygon"], camera["image_size"], size)):
            return z["id"]
    return None


def crop_zone(img: Image.Image, poly: list[Point], margin: int = 40) -> Image.Image:
    """Crop to the zone's bounding box (plus a margin) and grey out everything outside the zone."""
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    box = (max(0, int(min(xs)) - margin), max(0, int(min(ys)) - margin),
           min(img.width, int(max(xs)) + margin), min(img.height, int(max(ys)) + margin))
    region = img.crop(box).convert("RGB")
    mask = Image.new("L", region.size, 0)
    ImageDraw.Draw(mask).polygon([(x - box[0], y - box[1]) for x, y in poly], fill=255)
    out = Image.new("RGB", region.size, GREY)
    out.paste(region, (0, 0), mask)
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Make zone crops for an annotation session.")
    ap.add_argument("zones")
    ap.add_argument("image_list", help="CSV with slot_id, camera, file columns")
    ap.add_argument("images_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--skip", default="", help="comma-separated slot ids to leave out")
    a = ap.parse_args(argv[1:])
    cams = load_zones(Path(a.zones))
    skip = set(filter(None, a.skip.split(",")))
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    with Path(a.image_list).open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["slot_id"] in skip or row["camera"] not in cams:
                continue
            cam = cams[row["camera"]]
            with Image.open(Path(a.images_dir) / row["file"]) as img:
                for z in cam["zones"]:
                    poly = scaled(z["polygon"], cam["image_size"], img.size)
                    crop_zone(img, poly).save(out / f"{Path(row['file']).stem}__{z['id']}.jpg", quality=95)
                    n += 1
    print(f"{n} crops -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
