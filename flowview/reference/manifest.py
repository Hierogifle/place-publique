"""Build the frozen manifest of the reference set and check its coverage.

Images live outside Git (data/reference/images/). Each file is named after its plan slot and the
actual time of the image:  <slot_id>_<YYYYMMDD>-<HHMM>.jpg   e.g.  ARC-07_20260214-1205.jpg

The manifest (versioned) records, for every image: slot, strata, actual time, size, SHA-256 and a
difference hash used to flag near-duplicates. The weather column is filled by hand and preserved
across runs.

Usage:
    python -m flowview.reference.manifest data/reference/sampling_plan.csv data/reference/images data/reference/manifest.csv
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

from PIL import Image

NAME_RE = re.compile(r"^(?P<slot>[A-Z]{2,4}-R?\d{2})_(?P<date>\d{8})-(?P<hm>\d{4})\.(?:jpe?g|png)$", re.IGNORECASE)
WEATHER = ("beau", "couvert", "neige-brouillard", "nuit")
MANIFEST_FIELDS = ("slot_id", "subset", "camera", "crowd_level", "moment", "planned", "actual", "delta_min",
                   "file", "width", "height", "sha256", "dhash", "weather", "near_dup_of")
DHASH_W, DHASH_H = 16, 8      # 128 bits; wide grid because the images are panoramas
NEAR_DUP_MAX_BITS = 10        # to calibrate on the first real images


def parse_name(name: str) -> tuple[str, datetime] | None:
    m = NAME_RE.match(name)
    if not m:
        return None
    return m["slot"].upper(), datetime.strptime(m["date"] + m["hm"], "%Y%m%d%H%M")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def dhash(img: Image.Image, w: int = DHASH_W, h: int = DHASH_H) -> int:
    """Difference hash: compares neighbouring pixels of a tiny grayscale thumbnail."""
    small = img.convert("L").resize((w + 1, h), Image.Resampling.LANCZOS)
    px = small.tobytes()
    bits = 0
    for row in range(h):
        for col in range(w):
            left, right = px[row * (w + 1) + col], px[row * (w + 1) + col + 1]
            bits = (bits << 1) | (left > right)
    return bits


def hamming(a: int, b: int) -> int:
    return (a ^ b).bit_count()


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def build_manifest(plan_path: Path, images_dir: Path, previous: list[dict]) -> tuple[list[dict], list[str]]:
    plan = {r["slot_id"]: r for r in read_csv(plan_path)}
    kept_weather = {r["slot_id"]: r.get("weather", "") for r in previous}
    rows, problems = [], []
    for path in sorted(images_dir.glob("*")):
        if path.is_dir() or path.name.startswith("."):
            continue
        parsed = parse_name(path.name)
        if not parsed:
            problems.append(f"nom non conforme : {path.name}")
            continue
        slot_id, actual = parsed
        if slot_id not in plan:
            problems.append(f"créneau inconnu dans le plan : {path.name}")
            continue
        p = plan[slot_id]
        planned = datetime.fromisoformat(f"{p['date']}T{p['time_target']}")
        with Image.open(path) as img:
            width, height = img.size
            dh = dhash(img)
        rows.append({
            "slot_id": slot_id, "subset": p.get("subset", "reference"), "camera": p["camera"], "crowd_level": p["crowd_level"],
            "moment": p["moment"], "planned": planned.isoformat(timespec="minutes"),
            "actual": actual.isoformat(timespec="minutes"),
            "delta_min": round((actual - planned).total_seconds() / 60),
            "file": path.name, "width": width, "height": height, "sha256": sha256(path),
            "dhash": f"{dh:0{DHASH_W * DHASH_H // 4}x}", "weather": kept_weather.get(slot_id, ""),
            "near_dup_of": "",
        })
    # Near-duplicates: same camera, close hashes. Night images are expected to look alike: skipped.
    for i, a in enumerate(rows):
        for b in rows[:i]:
            same_scene = a["camera"] == b["camera"] and "nuit" not in (a["moment"], b["moment"])
            if same_scene and hamming(int(a["dhash"], 16), int(b["dhash"], 16)) <= NEAR_DUP_MAX_BITS:
                a["near_dup_of"] = b["slot_id"]
                problems.append(f"quasi-doublon : {a['slot_id']} ressemble à {b['slot_id']}")
                break
    seen = Counter(r["slot_id"] for r in rows)
    problems += [f"créneau en double : {s}" for s, n in seen.items() if n > 1]
    return rows, problems


def coverage(rows: list[dict], plan: list[dict], min_per_stratum: int = 10) -> list[str]:
    """Human-readable coverage report; lines starting with 'MANQUE' fail the step 1.2 criterion.

    The criterion applies to the reference subset only; the control subset is reported apart.
    """
    out = []
    control_plan = [p for p in plan if p.get("subset") == "control"]
    control_rows = [r for r in rows if r.get("subset") == "control"]
    plan = [p for p in plan if p.get("subset", "reference") == "reference"]
    rows = [r for r in rows if r.get("subset", "reference") == "reference"]
    cams = sorted({p["camera"] for p in plan})
    main_slots = {p["slot_id"] for p in plan if p["is_reserve"] == "0"}
    got = {r["slot_id"] for r in rows}
    out.append(f"images : {len(rows)} (créneaux principaux couverts : {len(main_slots & got)}/{len(main_slots)})")
    for cam in cams:
        c = Counter(r["crowd_level"] for r in rows if r["camera"] == cam)
        out.append(f"  {cam:12s} " + "  ".join(f"{k}={c.get(k, 0)}" for k in ("haute", "moyenne", "basse", "hors")))
        for k in ("haute", "moyenne", "basse"):
            if c.get(k, 0) < min_per_stratum:
                out.append(f"MANQUE {cam} / {k} : {c.get(k, 0)} < {min_per_stratum}")
    for field, values in (("moment", ("matin", "midi", "apres-midi", "nuit", "crepuscule")), ("weather", WEATHER)):
        c = Counter(r[field] for r in rows)
        out.append(f"  {field:12s} " + "  ".join(f"{v}={c.get(v, 0)}" for v in values)
                   + (f"  non renseigné={c.get('', 0)}" if field == "weather" else ""))
        need = values if field == "weather" else values[:3]
        for v in need:
            if c.get(v, 0) < min_per_stratum:
                out.append(f"MANQUE {field} / {v} : {c.get(v, 0)} < {min_per_stratum}")
    if control_plan:
        c_main = {p["slot_id"] for p in control_plan if p["is_reserve"] == "0"}
        c = Counter(r["camera"] for r in control_rows)
        out.append(f"contrôle : {len(control_rows)} images (créneaux couverts : "
                   f"{len(c_main & {r['slot_id'] for r in control_rows})}/{len(c_main)}) "
                   + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))
    missing = sorted(main_slots - got)
    if missing:
        out.append(f"créneaux principaux sans image ({len(missing)}) : " + ", ".join(missing[:20])
                   + (" …" if len(missing) > 20 else ""))
    return out


def write_manifest(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        w.writeheader()
        w.writerows(rows)


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__)
        return 2
    plan_path, images_dir, manifest_path = Path(argv[1]), Path(argv[2]), Path(argv[3])
    rows, problems = build_manifest(plan_path, images_dir, read_csv(manifest_path))
    write_manifest(rows, manifest_path)
    for line in problems + coverage(rows, read_csv(plan_path)):
        print(line)
    return 1 if any(p.startswith(("nom", "créneau")) for p in problems) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
