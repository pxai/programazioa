import json
import jokalaria

class Taldea:
    def karga(self):
        edukia = open("./jokalariak.json")
        jokalariak = json.load(edukia)
        print("Kargatuta:", jokalariak)
        self._jokalariak = []
        for j in jokalariak:
            self._jokalariak.append(jokalaria.Jokalaria(j["izena"], j["zenbakia"]))

    def fitxaketa(self, izena, dorsala):
        fitxategiBerria = jokalaria.Jokalaria(izena, dorsala)
        self._jokalariak.append(fitxategiBerria)

    def inprimatu(self):
        for jokalaria in self._jokalariak:
            print(jokalaria.toString())