from bank import value


def test_bank_default():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("grüezi") == 100


def test_bank_casesensitive():
    assert value("hEllO") == 0


def test_bank_int():
    assert value("0") == 100


def test_bank_special():
    assert value(".") == 100


def test_bank_mixed():
    assert value("hello.") == 0
