class Pilotoa:
    def __init__(self, izena):
        self._izena = izena

    @property
    def izena (self):
        return self._izena

    @izena.setter
    def izena (self, izena):
        self._izena = izena



class Hegazkina:
    def __init__(self, modeloa, pilotoa, koPilotoa):
        self._modeloa = modeloa
        self._pilotoa = pilotoa
        self._koPilotoa = koPilotoa

    @property
    def modeloa (self):
        return self._modeloa

    @modeloa.setter
    def modeloa (self, modeloa):
        self._modeloa = modeloa

    def info (self):
        return f"{self._modeloa} modeloa, {self._pilotoa.izena} eta {self._koPilotoa.izena}rekin hegaldia egiten"


pilotoa1 = Pilotoa("Han Solo")
pilotoa2 = Pilotoa("Murdock")
hegazkinTxikia = Hegazkina("AirBluff 727", pilotoa1, pilotoa2)

print(hegazkinTxikia.info())
