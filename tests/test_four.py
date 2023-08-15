def test_equalto():
    assert 5 == 2 + 3, "do you know maths?"

def test_greaterthan_lesserthan():
    num = 42
    assert num > 32 and num < 52, f"num expected to be greater than 32 and lesser than 52, got{num}"

def test_in_iterable():
    fruits = ['apple', 'pear', 'grape']
    assert 'pear' in fruits
    assert 'blueberry' in fruits