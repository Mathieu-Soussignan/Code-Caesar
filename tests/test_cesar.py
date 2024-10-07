from app.cesar import chiffrement_cesar, dechiffrement_cesar

def test_chiffrement_cesar():
    assert chiffrement_cesar("ABC", 3) == "DEF"
    assert chiffrement_cesar("XYZ", 3) == "ABC"
    assert chiffrement_cesar("Bonjour, tout le monde !", 3) == "Erqmrxu, wrxw oh prqgh !"

def test_dechiffrement_cesar():
    assert dechiffrement_cesar("DEF", 3) == "ABC"
    assert dechiffrement_cesar("Erqmrxu, wrxw oh prqgh !", 3) == "Bonjour, tout le monde !"