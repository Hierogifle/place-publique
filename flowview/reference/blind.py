"""Draw the blind-count subset used to measure anchoring bias (ADR 0025).

A seeded, per-camera random draw among the collected reference images (main slots only, night
images excluded: nothing to count). These images are counted by hand *without* pre-annotation
first, then again with it, at least a day later.

Usage:
    python -m flowview.reference.blind data/reference/manifest.csv data/reference/blind_set.csv [--per-camera 8]
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

SEED = 20261119      # distinct from the sampling-plan seed


def draw_blind_set(manifest_rows: list[dict], per_camera: int, seed: int = SEED) -> list[dict]:
    rng = random.Random(seed)
    eligible = [r for r in manifest_rows
                if r.get("subset", "reference") == "reference" and "-R" not in r["slot_id"]
                and r["moment"] != "nuit"]
    out = []
    for cam in sorted({r["camera"] for r in eligible}):
        pool = sorted((r for r in eligible if r["camera"] == cam), key=lambda r: r["slot_id"])
        k = min(per_camera, len(pool))
        out += sorted(rng.sample(pool, k), key=lambda r: r["slot_id"])
    return [{"slot_id": r["slot_id"], "camera": r["camera"], "file": r["file"]} for r in out]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Draw the blind-count subset.")
    ap.add_argument("manifest")
    ap.add_argument("out")
    ap.add_argument("--per-camera", type=int, default=8)
    a = ap.parse_args(argv[1:])
    with Path(a.manifest).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    chosen = draw_blind_set(rows, a.per_camera)
    with Path(a.out).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=("slot_id", "camera", "file"))
        w.writeheader()
        w.writerows(chosen)
    print(f"{len(chosen)} images à compter sans aide -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
