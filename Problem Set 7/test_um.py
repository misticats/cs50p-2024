from um import count


def test_count_once():
    assert count("hello, um, world") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album...") == 1


def test_count_twice():
    assert count("Um, thanks, um...") == 2


def test_count_dont():
    assert count("yummy") == 0


