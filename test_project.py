import pytest
from pathlib import Path
from project import convert_to_path


def test_relative_path():
    assert convert_to_path("Downloads") == Path.home() / "Downloads"


def test_nested_relative_path():
    assert convert_to_path("Projects/MyGame") == Path.home() / "Projects" / "MyGame"


def test_absolute_path():
    absolute = Path("/tmp")
    assert convert_to_path("/tmp") == absolute


def test_expanduser():
    assert convert_to_path("~/Downloads") == Path.home() / "Downloads"


def test_invalid_type():
    with pytest.raises(SystemExit):
        convert_to_path(None)