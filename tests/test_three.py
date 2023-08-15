def test_name():
    name = 'muralikrishnan'
    assert name is 'muralikrishnan' and isinstance(name, str), \
        f"you are not {name}"

def test_isinstance():
    num = 21
    assert isinstance(num, int)
    num = 32.0
    assert isinstance(num, float)
    name = 'murali'
    assert isinstance(name, str)
    