"""Stratified, seeded sampling plan for the reference set.

The plan is drawn *before* any image is looked at, so that nobody picks "nice" images by hand.
Each slot is a (camera, date, target time) with its strata: expected crowd level (a calendar
proxy: school holidays, weekends) and moment of the day. Two subsets:
  - reference: the cameras the error is measured on (and the acceptability threshold set on);
  - control:   a few images from other cameras, to check that the model holds on unseen views.

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
WEEKDAYS = ("lun", "mar", "mer", "jeu", "ven", "sam", "dim")
PLAN_FIELDS = ("slot_id", "subset", "camera", "camera_name", "date", "weekday", "time_target",
               "crowd_level", "moment", "is_reserve", "viewer")


@dataclass(frozen=True)
class Slot:
    slot_id: str
    subset: str          # reference / control
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


def _sample_camera(rng: random.Random, cfg: dict, cam: dict, quotas: dict, n_reserve: int,
                   subset: str) -> list[Slot]:
    days = season_days(cfg)
    moments = list(cfg["moments"])
    step = cfg["time_step_minutes"]
    used: set[date] = set()
    drafts: list[tuple[date, str, str]] = []          # (day, crowd level, moment)

    def slot(slot_id: str, d: date, lvl: str, m: str, reserve: bool) -> Slot:
        windows = cfg["off_hours"][m] if m in OFF_HOURS else [cfg["moments"][m]]
        return Slot(slot_id, subset, cam["id"], cam["name"], d.isoformat(), WEEKDAYS[d.weekday()],
                    random_time(rng, windows, step), lvl, m, reserve, cam["viewer"])

    # Opening hours: one image per day at most, moments spread evenly within each crowd level.
    for lvl in CROWD_LEVELS:
        k = quotas[lvl]
        pool = [d for d in days if crowd_level(d, cfg) == lvl and d not in used]
        if k > len(pool):
            raise ValueError(f"{cam['id']}: {k} images asked for level {lvl}, only {len(pool)} days")
        order = (moments * (k // len(moments) + 1))[:k]
        rng.shuffle(order)
        for d, m in zip(sorted(rng.sample(pool, k)), order):
            used.add(d)
            drafts.append((d, lvl, m))

    # Off hours (night, twilight): empty or dark scenes, to measure false positives.
    for m in OFF_HOURS:
        pool = [d for d in days if d not in used]
        for d in sorted(rng.sample(pool, quotas.get(m, 0))):
            used.add(d)
            drafts.append((d, "hors", m))

    drafts.sort()
    slots = [slot(f"{cam['code']}-{i:02d}", d, lvl, m, False) for i, (d, lvl, m) in enumerate(drafts, 1)]

    # Reserve: replaces a missing image or a near-duplicate, used in order, same camera.
    pool = [d for d in days if d not in used]
    for i, d in enumerate(sorted(rng.sample(pool, n_reserve)), 1):
        slots.append(slot(f"{cam['code']}-R{i:02d}", d, crowd_level(d, cfg), rng.choice(moments), True))
    return slots


def build_plan(cfg: dict) -> list[Slot]:
    rng = random.Random(cfg["seed"])
    slots: list[Slot] = []
    for cam in cfg["cameras"]:
        slots += _sample_camera(rng, cfg, cam, cfg["quotas_per_camera"], cfg["reserve_per_camera"],
                                "reference")
    for cam in cfg.get("control_cameras", []):
        slots += _sample_camera(rng, cfg, cam, cfg["control_quotas_per_camera"],
                                cfg["control_reserve_per_camera"], "control")
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
    for subset in ("reference", "control"):
        main_n = sum(s.subset == subset and not s.is_reserve for s in slots)
        res_n = sum(s.subset == subset and s.is_reserve for s in slots)
        print(f"{subset}: {main_n} slots + {res_n} reserve")
    print(f"{datetime.now():%Y-%m-%d %H:%M} plan written -> {argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
