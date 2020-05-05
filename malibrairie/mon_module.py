from ._mes_decorateurs import mondecorateur_avant, mondecorateur_apres


class MaClasse:
    def __init__(self):
        pass

    @mondecorateur_avant
    @mondecorateur_apres
    def get(self, url):
        return url
