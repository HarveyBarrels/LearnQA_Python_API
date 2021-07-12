import  pytest

def test_short_phrase():
    phrase = input("Set a phrase:\n")

    assert len(phrase) < 15, "Phrase has more than 15 symbols"
