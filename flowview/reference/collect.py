"""Collect the reference images listed in the sampling plan from the official webcam archive.

Scope (ADR 0024): for each planned slot, fetch the day index that the official viewer loads itself
for that camera and date, then download the single image closest to the target time. Nothing else:
no enumeration, no guessing, one request at a time, a fixed delay between requests.

Images go to data/reference/images/ (outside Git), named <slot_id>_<YYYYMMDD>-<HHMM>.jpg with the
local time of the image. Each attempt is logged in data/reference/collect_log.csv (versioned).

Usage:
    python -m flowview.reference.collect configs/reference_lesarcs.json data/reference/sampling_plan.csv \
        data/reference/images data/reference/collect_log.csv [--reserves SLOT,SLOT,...] [--limit N]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

USER_AGENT = "FlowView-school-project/0.1 (pedagogical use, few images)"
LOG_FIELDS = ("when", "slot_id", "camera", "planned", "status", "actual", "delta_min", "file", "url")


def _get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def closest_image(day_index: dict, target: datetime, tz: ZoneInfo, key: str) -> tuple[dict, datetime] | None:
    """Image of the day index whose local time is closest to the target (local, naive)."""
    best = None
    for img in (day_index or {}).get("images", []):
        stamp = datetime.strptime(img["stamp"], "%Y%m%dT%H%M%SZ").replace(tzinfo=UTC)
        local = stamp.astimezone(tz).replace(tzinfo=None)
        if key not in img:
            continue
        gap = abs((local - target).total_seconds())
        if best is None or gap < best[0]:
            best = (gap, img, local)
    return (best[1], best[2]) if best else None


def collect(cfg: dict, plan: list[dict], images_dir: Path, log_path: Path, slot_ids: set[str] | None,
            limit: int | None, fetch=_get, sleep=time.sleep) -> list[dict]:
    arch = cfg["archive"]
    tz = ZoneInfo(arch["timezone"])
    cams = {c["id"]: c for c in cfg["cameras"] + cfg.get("control_cameras", [])}
    images_dir.mkdir(parents=True, exist_ok=True)
    done = {p.name.split("_")[0] for p in images_dir.glob("*.jpg")}
    todo = [p for p in plan if (p["slot_id"] in slot_ids if slot_ids else p["is_reserve"] == "0")
            and p["slot_id"] not in done]
    if limit is not None:
        todo = todo[:limit]
    log: list[dict] = []
    for i, p in enumerate(todo):
        cam = cams[p["camera"]]
        target = datetime.fromisoformat(f"{p['date']}T{p['time_target']}")
        entry = {"when": datetime.now().isoformat(timespec="seconds"), "slot_id": p["slot_id"],
                 "camera": p["camera"], "planned": target.isoformat(timespec="minutes"), "status": "",
                 "actual": "", "delta_min": "", "file": "", "url": ""}
        try:
            index_url = arch["day_index"].format(date=p["date"], **cam)
            found = closest_image(json.loads(fetch(index_url)), target, tz, arch["image_key"])
            sleep(arch["delay_seconds"])
            if not found:
                entry["status"] = "absent (archive vide)"
            else:
                img, local = found
                delta = round((local - target).total_seconds() / 60)
                entry.update(actual=local.isoformat(timespec="minutes"), delta_min=delta, url=img[arch["image_key"]])
                if abs(delta) > arch["max_gap_minutes"]:
                    entry["status"] = f"absent (image la plus proche à {delta} min)"
                else:
                    name = f"{p['slot_id']}_{local:%Y%m%d-%H%M}.jpg"
                    (images_dir / name).write_bytes(fetch(img[arch["image_key"]]))
                    entry.update(status="ok", file=name)
                    sleep(arch["delay_seconds"])
        except (OSError, ValueError, KeyError) as exc:   # logged, the run goes on
            entry["status"] = f"erreur : {type(exc).__name__} {getattr(exc, 'code', '')}".strip()
            sleep(arch["delay_seconds"])
        log.append(entry)
        print(f"[{i + 1}/{len(todo)}] {entry['slot_id']} {entry['status']} {entry['file']}", flush=True)
    write_log(log, log_path)
    return log


def write_log(entries: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if new:
            w.writeheader()
        w.writerows(entries)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Collect the reference images of the sampling plan.")
    ap.add_argument("config")
    ap.add_argument("plan")
    ap.add_argument("images_dir")
    ap.add_argument("log")
    ap.add_argument("--reserves", help="comma-separated reserve slots to fetch instead of the main slots")
    ap.add_argument("--limit", type=int, help="fetch at most N slots (for a first check)")
    a = ap.parse_args(argv[1:])
    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    with Path(a.plan).open(encoding="utf-8", newline="") as f:
        plan = list(csv.DictReader(f))
    slot_ids = set(a.reserves.split(",")) if a.reserves else None
    log = collect(cfg, plan, Path(a.images_dir), Path(a.log), slot_ids, a.limit)
    print(f"{sum(e['status'] == 'ok' for e in log)}/{len(log)} images collectées")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
