"""Tests for the archive collector (no network: the fetch function is faked)."""
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from flowview.reference import collect

CFG = json.loads((Path(__file__).parents[1] / "configs" / "reference_lesarcs.json").read_text(encoding="utf-8"))
INDEX = {"images": [
    {"stamp": "20260214T103000Z", "url_mega": "https://example.test/a.jpg"},   # 11:30 Paris
    {"stamp": "20260214T110500Z", "url_mega": "https://example.test/b.jpg"},   # 12:05 Paris
]}


def test_closest_image_uses_local_time():
    img, local = collect.closest_image(INDEX, datetime(2026, 2, 14, 12, 0), ZoneInfo("Europe/Paris"), "url_mega")
    assert img["url_mega"].endswith("b.jpg") and local == datetime(2026, 2, 14, 12, 5)


def test_collect_downloads_only_planned_slots(tmp_path):
    plan = [{"slot_id": "ARC-01", "camera": "arcabulle", "date": "2026-02-14", "time_target": "12:00",
             "is_reserve": "0"},
            {"slot_id": "ARC-R01", "camera": "arcabulle", "date": "2026-02-15", "time_target": "12:00",
             "is_reserve": "1"}]
    calls = []

    def fake_fetch(url):
        calls.append(url)
        return json.dumps(INDEX).encode() if "/day/" in url else b"jpeg-bytes"

    log = collect.collect(CFG, plan, tmp_path / "img", tmp_path / "log.csv", None, None,
                          fetch=fake_fetch, sleep=lambda s: None)
    assert [e["status"] for e in log] == ["ok"]
    assert (tmp_path / "img" / "ARC-01_20260214-1205.jpg").read_bytes() == b"jpeg-bytes"
    assert len(calls) == 2 and "/day/2026-02-14" in calls[0]
    # A second run skips what is already there.
    assert collect.collect(CFG, plan, tmp_path / "img", tmp_path / "log.csv", None, None,
                           fetch=fake_fetch, sleep=lambda s: None) == []


def test_slot_too_far_from_any_image_is_absent(tmp_path):
    plan = [{"slot_id": "ARC-02", "camera": "arcabulle", "date": "2026-02-14", "time_target": "16:00",
             "is_reserve": "0"}]
    log = collect.collect(CFG, plan, tmp_path / "img", tmp_path / "log.csv", None, None,
                          fetch=lambda u: json.dumps(INDEX).encode(), sleep=lambda s: None)
    assert log[0]["status"].startswith("absent")
