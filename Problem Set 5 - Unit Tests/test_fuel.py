import fuel
import pytest


def test_fuel_convert():
    assert fuel.convert("10/20") == 50
    with pytest.raises(ValueError):  # Testing for exception
        fuel.convert("cat/dog")
    with pytest.raises(ZeroDivisionError):  # Testing for exception
        fuel.convert("10/0")


def test_fuel_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
