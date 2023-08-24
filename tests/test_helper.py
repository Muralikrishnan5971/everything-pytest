import pytest
from cards import Card

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True	# hides the function in the traceback
    assert c1 == c2		# assert c1 == c2 is used to check everything except the id for equality
    if c1.id != c2.id:
        pytest.fail(f"id's don't match. {c1.id} != {c2.id}")

def test_identical():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=123)
    assert_identical(c1, c2)

def test_identical_fail():
    c1 = Card("foo", id=123)
    c2 = Card("foo", id=43)
    assert_identical(c1, c2)