from twttr import shorten


def test_shorten_str():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"


def test_shorten_int():
    assert shorten("Twitter0") == "Twttr0"


def test_shorten_specialchar():
    assert shorten("Twitter.") == "Twttr."

