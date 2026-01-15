from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4.5") == False


def test_validate_1():
    assert validate("268.255.255.0") == False
    assert validate("10.0.0.0") == True
    assert validate("172.16.0.0") == True
    assert validate("192.168.1.1") == True

def test_validate_4():
    assert validate("0.0.0.255") == True
    assert validate("0.0.0.256") == False
