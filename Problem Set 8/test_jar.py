from jar import Jar
import pytest


def test_init():
    # initialize jar object, starting capacity (10), default size(0)
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # initialize jar object, using default value (12), default size(0)
    jar = Jar()
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("cat")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    # initialize jar object, starting capacity (5), default size(0)
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    # initialize jar object, starting capacity (5), default size(0)
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(4)
