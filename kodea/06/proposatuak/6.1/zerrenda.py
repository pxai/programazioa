import json

class Zerrenda:
    def __init__ (self, fitxategiIzena):
        edukia = open(fitxategiIzena, "r")
        self._datuak = json.load(edukia)
        edukia.close()

    def existitzenDa (self, izena):
        for datu in self._datuak:
            if datu["izena"] == izena:
                return True

        return False

    def xehetu (self):
        self._datuak = list(map(lambda datu: { "id": datu["id"], "izena": datu["izena"].lower() }, self._datuak))

    def posizioa (self, izena):
        i = 0
        for datu in self._datuak:
            if datu["izena"] == izena:
                return i
            i += 1
        return -1

    def inprimatu (self):
        for datu in self._datuak:
            print(datu)