from twttr import shorten
def test_shorten():
    assert shorten("znba") == "znb"
    assert shorten("hello") == "hll"
    assert shorten("python") == "pythn"
    assert shorten("aeiou") == ""
    assert shorten("bcd") == "bcd"
    assert shorten("") == ""

test_shorten()
