"""Tests for the reference set tooling (sampling plan and manifest)."""
import json
from datetime import date
from pathlib import Path

from PIL import Image

from flowview.reference import manifest, sampling

CFG = json.loads((Path(__file__).parents[1] / "configs" / "reference_lesarcs.json").read_text(encoding="utf-8"))


def test_plan_is_deterministic():
    assert sampling.build_plan(CFG) == sampling.build_plan(CFG)


def test_plan_quotas_and_one_image_per_day_per_camera():
    slots = sampling.build_plan(CFG)
    groups = (("reference", CFG["cameras"], CFG["quotas_per_camera"], CFG["reserve_per_camera"]),
              ("control", CFG["control_cameras"], CFG["control_quotas_per_camera"],
               CFG["control_reserve_per_camera"]))
    for subset, cams, quotas, n_reserve in groups:
        for cam in cams:
            main = [s for s in slots if s.camera == cam["id"] and not s.is_reserve]
            reserve = [s for s in slots if s.camera == cam["id"] and s.is_reserve]
            assert all(s.subset == subset for s in main + reserve)
            assert len(main) == sum(quotas.values())
            assert len(reserve) == n_reserve
            days = [s.date for s in main + reserve]
            assert len(days) == len(set(days))
            for lvl in sampling.CROWD_LEVELS:
                assert sum(s.crowd_level == lvl for s in main) == quotas[lvl]


def test_plan_stays_in_season_and_time_windows():
    start, end = CFG["season"]["start"], CFG["season"]["end"]
    for s in sampling.build_plan(CFG):
        assert start <= s.date <= end
        if s.moment in CFG["moments"]:
            a, b = CFG["moments"][s.moment]
            assert a <= s.time_target <= b
        if s.moment == "nuit":
            assert s.time_target >= "22:00" or s.time_target <= "05:00"


def test_crowd_level_calendar_proxy():
    assert sampling.crowd_level(date(2026, 2, 14), CFG) == "haute"     # winter holidays, 2 zones
    assert sampling.crowd_level(date(2026, 1, 17), CFG) == "moyenne"   # Saturday out of holidays
    assert sampling.crowd_level(date(2026, 1, 13), CFG) == "basse"     # Tuesday out of holidays


def test_parse_name():
    slot, when = manifest.parse_name("ARC-07_20260214-1205.jpg")
    assert slot == "ARC-07" and when.isoformat() == "2026-02-14T12:05:00"
    assert manifest.parse_name("GRZ-R03_20260101-0930.JPG")[0] == "GRZ-R03"
    assert manifest.parse_name("photo.jpg") is None


def test_dhash_identical_and_different_images():
    a = Image.linear_gradient("L").rotate(90).resize((400, 100))
    b = a.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    assert manifest.hamming(manifest.dhash(a), manifest.dhash(a.copy())) == 0
    assert manifest.hamming(manifest.dhash(a), manifest.dhash(b)) > manifest.NEAR_DUP_MAX_BITS


def test_manifest_flags_bad_names_and_keeps_weather(tmp_path):
    plan_path = tmp_path / "plan.csv"
    sampling.write_plan(sampling.build_plan(CFG), plan_path)
    slot = next(s for s in sampling.build_plan(CFG) if s.slot_id == "ARC-01")
    images = tmp_path / "images"
    images.mkdir()
    Image.new("RGB", (60, 20), "white").save(images / f"ARC-01_{slot.date.replace('-', '')}-1200.jpg")
    Image.new("RGB", (60, 20), "white").save(images / "random.jpg")
    previous = [{"slot_id": "ARC-01", "weather": "beau"}]
    rows, problems = manifest.build_manifest(plan_path, images, previous)
    assert len(rows) == 1 and rows[0]["weather"] == "beau"
    assert any("nom non conforme" in p for p in problems)
