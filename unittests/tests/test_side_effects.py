from sideeffects import hello

def test_default():
    assert hello() == "hello world"

def test_arg():
    assert hello("jai") == "hello jai"