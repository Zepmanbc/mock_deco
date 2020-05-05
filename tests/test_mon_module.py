from malibrairie.mon_module import MaClasse


def test_standard_use():
    inst = MaClasse()
    result = inst.get("google")
    assert result == "https://google.com"


def test_fuck_deco():  # FAIL
    inst = MaClasse()
    result = inst.get("google")
    assert result == "google"


def test_avec_les__wrapped__():
    while hasattr(MaClasse.get, "__wrapped__"):
        MaClasse.get = MaClasse.get.__wrapped__

    inst = MaClasse()
    result = inst.get("google")
    assert result == "google"
