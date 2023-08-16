import pytest
from cards import Card

def test_with_fail():
    c1 = Card("sit", "murali")
    c2 = Card("do something", "krishnan")
    if c1 != c2:
        pytest.fail("they dont match")