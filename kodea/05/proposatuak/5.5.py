class Jokalaria:
    def __init__(self, izena, posizioa, zenbakia):
        self._izena = izena
        self._posizioa = posizioa
        self._zenbakia = zenbakia

    def txosten (self):
        return f"{self._izena} {self._posizioa} {self._zenbakia}"


class Taldea:
    def __init__ (self, izena, sortzea, aurrekontua):
        self._izena = izena
        self._sortzea = sortzea
        self._aurrekontua = aurrekontua
        self._jokalariak = []

    def jokalariaFitxatu (self, jokalaria):
        self._jokalariak.append(jokalaria)

    def jokalariakErakutsi (self):
        for jokalaria in self._jokalariak:
            print(jokalaria.txosten())


jokalaria1 = Jokalaria("Maradona", "Aurrelari", 10)
jokalaria2 = Jokalaria("Beckenbauer", "Defentsa", 4)

print(jokalaria1.txosten())

ekipoa = Taldea("New Team", 1983, 39944.45)
ekipoa.jokalariaFitxatu(jokalaria1)
ekipoa.jokalariaFitxatu(jokalaria2)

ekipoa.jokalariakErakutsi()