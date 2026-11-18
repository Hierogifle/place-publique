"""Stratified, seeded sampling plan for the reference set.

The plan is drawn *before* any image is looked at, so that nobody picks "nice" images by hand.
Each slot is a (camera, date, target time) with its strata: expected crowd level (a calendar
proxy: school holidays, weekends) and moment of the day. Images are then collected by hand from
the official webcam viewer, as close as possible to the target time.

Usage:
    python -m flowview.reference.sampling configs/reference_lesarcs.json data/reference/sampling_plan.csv
"""
from __future__ import annotations

import csv
import json
import random
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path

CROWD_LEVELS = ("haute", "moyenne", "basse")
OFF_HOURS = ("nuit", "crepuscule")
PLAN_FIELDS = ("slot_id", "camera", "camera_name", "date", "weekday", "time_target",
               "crowd_level", "moment", "is_reserve", "viewer")


@dataclass(frozen=True)
class Slot:
    slot_id: str
    camera: str
    camera_name: str
    date: str
    weekday: str
    time_target: str
    crowd_level: str     # haute / moyenne / basse (calendar proxy), or "hors" for off hours
    moment: str          # matin / midi / apres-midi / nuit / crepuscule
    is_reserve: bool
    viewer: str


def _d(s: str) -> date:
    return date.fromisoformat(s)


def _t(s: str) -> time:
    return time.fromisoformat(s)


def _in_ranges(day: date, ranges: list[list[str]]) -> bool:
    return any(_d(a) <= day <= _d(b) for a, b in ranges)


def crowd_level(day: date, cfg: dict) -> str:
    """Expected crowd level for a day: a calendar proxy, checked later against hand counts."""
    if _in_ranges(day, cfg["high_periods"]):
        return "haute"
    if _in_ranges(day, cfg["holidays"]) or day.weekday() >= 5:
        return "moyenne"
    return "basse"


def season_days(cfg: dict) -> list[date]:
    start, end = _d(cfg["season"]["start"]), _d(cfg["season"]["end"])
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]


def random_time(rng: random.Random, windows: list[list[str]], step: int) -> str:
    """Uniform time inside one of the windows (picked proportionally to its length), on a step grid."""
    spans = []
    for a, b in windows:
        t0, t1 = _t(a), _t(b)
        m0, m1 = t0.hour * 60 + t0.minute, t1.hour * 60 + t1.minute
        if m1 <= m0:
            raise ValueError(f"window {a}-{b} must not cross midnight: split it in two")
        spans.append((m0, m1))
    total = sum(m1 - m0 for m0, m1 in spans)
    x = rng.uniform(0, total)
    for m0, m1 in spans:
        if x <= m1 - m0:
            minute = int((m0 + x) // step * step)
            return f"{minute // 60:02d}:{minute % 60:02d}"
        x -= m1 - m0
    m0, _ = spans[-1]
    return f"{m0 // 60:02d}:{m0 % 60:02d}"


def build_plan(cfg: dict) -> list[Slot]:
    rng = random.Random(cfg["seed"])
    days = season_days(cfg)
    by_level = {lvl: [d for d in days if crowd_level(d, cfg) == lvl] for lvl in CROWD_LEVELS}
    moments = list(cfg["moments"])
    step = cfg["time_step_minutes"]
    weekdays = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
    slots: list[Slot] = []

    for cam in cfg["cameras"]:
        used: set[date] = set()
        drafts: list[tuple[date, str, str]] = []      # (day, crowd level, moment)

        # Opening hours: one image per day at most, moments spread evenly within each crowd level.
        for lvl in CROWD_LEVELS:
            k = cfg["quotas_per_camera"][lvl]
            pool = [d for d in by_level[lvl] if d not in used]
            picked = sorted(rng.sample(pool, k))
            order = (moments * (k // len(moments) + 1))[:k]
            rng.shuffle(order)
            for d, m in zip(picked, order):
                used.add(d)
                drafts.append((d, lvl, m))

        # Off hours (night, twilight): empty or dark scenes, to measure false positives.
        for moment in OFF_HOURS:
            k = cfg["quotas_per_camera"][moment]
            pool = [d for d in days if d not in used]
            for d in sorted(rng.sample(pool, k)):
                used.add(d)
                drafts.append((d, "hors", moment))

        drafts.sort()
        for i, (d, lvl, m) in enumerate(drafts, 1):
            windows = cfg["off_hours"][m] if m in OFF_HOURS else [cfg["moments"][m]]
            slots.append(Slot(f"{cam['code']}-{i:02d}", cam["id"], cam["name"], d.isoformat(),
                              weekdays[d.weekday()], random_time(rng, windows, step), lvl, m, False,
                              cam["viewer"]))

        # Reserve: replaces a missing image or a near-duplicate, used in order, same camera.
        pool = [d for d in days if d not in used]
        for i, d in enumerate(sorted(rng.sample(pool, cfg["reserve_per_camera"])), 1):
            m = rng.choice(moments)
            slots.append(Slot(f"{cam['code']}-R{i:02d}", cam["id"], cam["name"], d.isoformat(),
                              weekdays[d.weekday()], random_time(rng, [cfg["moments"][m]], step),
                              crowd_level(d, cfg), m, True, cam["viewer"]))
    return slots


def write_plan(slots: list[Slot], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=PLAN_FIELDS)
        w.writeheader()
        for s in slots:
            row = asdict(s)
            row["is_reserve"] = int(s.is_reserve)
            w.writerow(row)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    cfg = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    slots = build_plan(cfg)
    write_plan(slots, Path(argv[2]))
    main_slots = [s for s in slots if not s.is_reserve]
    print(f"{datetime.now():%Y-%m-%d %H:%M} plan written: {len(main_slots)} slots + "
          f"{len(slots) - len(main_slots)} reserve -> {argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
