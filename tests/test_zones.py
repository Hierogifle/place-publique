"""Tests for counting zones."""
from pathlib import Path

from PIL import Image

from flowview import zones

CAMS = zones.load_zones(Path(__file__).parents[1] / "configs" / "zones_lesarcs.json")
SQUARE = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]


def test_point_in_polygon():
    assert zones.point_in_polygon((5, 5), SQUARE)
    assert not zones.point_in_polygon((15, 5), SQUARE)


def test_first_zone_wins_and_outside_is_none():
    cam = {"image_size": [100, 100], "zones": [
        {"id": "A", "polygon": [[0, 0], [60, 0], [60, 100], [0, 100]]},
        {"id": "B", "polygon": [[40, 0], [100, 0], [100, 100], [40, 100]]}]}
    assert zones.zone_of((50, 50), cam, (100, 100)) == "A"
    assert zones.zone_of((80, 50), cam, (100, 100)) == "B"
    assert zones.zone_of((50, 50), cam, (200, 200)) == "A"     # polygons scale with the image
    cam["zones"] = cam["zones"][:1]
    assert zones.zone_of((80, 50), cam, (100, 100)) is None


def test_crop_greys_outside_the_zone():
    img = Image.new("RGB", (100, 100), (255, 0, 0))
    out = zones.crop_zone(img, [(20, 20), (80, 20), (20, 80)], margin=0)
    assert out.size == (60, 60)
    assert out.getpixel((2, 2)) == (255, 0, 0)        # inside the triangle
    assert out.getpixel((58, 58)) == zones.GREY        # outside


def test_config_has_the_three_reference_cameras():
    assert set(CAMS) == {"arcabulle", "grizzly", "mont-blanc"}
    assert all(len(z["polygon"]) >= 3 for c in CAMS.values() for z in c["zones"])
