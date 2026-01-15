import plates


def test_plates_default():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50P") == False
    assert plates.is_valid("PI3.14") == False
    assert plates.is_valid("H") == False
    assert plates.is_valid("OUTATIME") == False


def test_plates_begin():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("00CS50") == False
    assert plates.is_valid("9ABC")  == False
    assert plates.is_valid("A1234")  == False
    assert plates.is_valid(" 123AB")  == False
    assert plates.is_valid("")  == False


def test_plates_zero():
    assert plates.is_valid("0AA222") == False


def test_plates_period():
    assert plates.is_valid("AAA.22") == False


def test_plates_space():
    assert plates.is_valid("AAA 22") == False
