from seasons import get_date
import pytest


def test_seasons_default():
    assert get_date("2023-01-08") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_date("2022-01-08") == "One million, fifty-one thousand, two hundred minutes"


def test_seasons_invalid():
    with pytest.raises(SystemExit):
        get_date("2025-01-08")
    with pytest.raises(SystemExit):
        get_date("2023-13-08")
    with pytest.raises(SystemExit):
        get_date("2023-12-32")
