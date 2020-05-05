from malibrairie.mon_module import MaClasse


def test_fuck_deco():
    inst = MaClasse()
    result = inst.get("google")
    assert result == "google"


def test_avec_les__wrapped__():
    while hasattr(MaClasse.get, "__wrapped__"):
        MaClasse.get = MaClasse.get.__wrapped__

    inst = MaClasse()
    result = inst.get("google")
    assert result == "google"
