def test_object_assertions():
    x = 1
    y = x
    null = None
    assert x is y
    assert null is None
    # assert x is not y

def test_all_iterable():
    movies = ['forest gump', 'in the mood for love', 'reservoir dogs']
    assert all(movies)
    
def test_any_iterable():
    items = [1, 0, "", False]
    assert any(items)
