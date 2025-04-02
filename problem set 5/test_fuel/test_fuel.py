import fuel as W
def test_convert():
    assert W.convert("x/y")=="value error"
    assert W.convert("1/4")==25
    assert W.convert("4/4")==100
    assert W.convert("2/4")==50
def test_gauge():
    assert W.gauge(100)=="F"
    assert W.gauge(0)=="E"
    assert W.gauge(50)=="50%"
    assert W.gauge(99)=="F"
test_convert()
test_gauge()
