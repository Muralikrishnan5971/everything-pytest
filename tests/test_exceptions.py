import cards
import pytest

def test_no_path_raiser():
    with pytest.raises(TypeError):
        cards.CardsDB()
        
def test_raises_with_info():
    """
    the match parameter takes a regular experession adn matches it with the exception message.
    """
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()

def test_raises_with_info_alt():
    """
    We can use exc_info or any other variable name to interorogate extra parameters to the
    exception if its a custom exception. The exc_info will be of type Exceptioninfo
    """
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(exc_info.value)
