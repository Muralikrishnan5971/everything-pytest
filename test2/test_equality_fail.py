from cards import Card

def test_equality_fail():
	c1 = Card("somethin", "murali", "todo", 123)
	c2= Card("something", "krishnan", "done", 123)
	assert c1 == c2

if __name__ == "__main__":
	test_equality_fail()