"""Tests for the pre-annotation helpers (no model needed)."""
from flowview import preannotate as pa


def test_tiles_cover_the_image_with_overlap():
    t = pa.tiles(3000, 1000, 1280, 0.25)
    assert t[0][:2] == (0, 0)
    assert max(x1 for _, _, x1, _ in t) == 3000 and max(y1 for _, _, _, y1 in t) == 1000
    assert all(x1 - x0 <= 1280 and y1 - y0 <= 1280 for x0, y0, x1, y1 in t)


def test_nms_merges_duplicates_from_overlapping_tiles():
    a = {"cls": 0, "conf": 0.9, "box": [0, 0, 10, 20]}
    b = {"cls": 0, "conf": 0.6, "box": [1, 0, 11, 20]}
    c = {"cls": 2, "conf": 0.5, "box": [1, 0, 11, 20]}
    assert pa.nms([a, b, c]) == [a, c]


def test_people_are_qualified_by_their_equipment():
    person = {"cls": pa.PERSON, "conf": 0.8, "box": [100, 100, 120, 160]}
    skis = {"cls": pa.SKIS, "conf": 0.5, "box": [95, 150, 125, 165]}
    lone = {"cls": pa.PERSON, "conf": 0.8, "box": [300, 100, 320, 160]}
    car = {"cls": 2, "conf": 0.7, "box": [500, 100, 560, 140]}
    labels = [d["label"] for d in pa.classify_people([person, skis, lone, car])]
    assert labels == ["skieur", "pieton", "voiture"]
