class Ibilgailua:
    def __init__(self, matrikula):
        self._matrikula = matrikula

    @property
    def matrikula (self):
        return self._matrikula

    @matrikula.setter
    def matrikula (self, matrikula):
        self._matrikula = matrikula

    def abiarazi (self):
        print("Abiarazten ", self._matrikula)


class Kotxea(Ibilgailua):
    def __init__(self, matrikula, modeloa, kolorea):
        super().__init__(matrikula)
        self._modeloa = modeloa
        self._kolorea = kolorea

    def info (self):
        return f"{self.matrikula} {self._modeloa} {self._kolorea}";


kotxea = Kotxea("0042ASI", "Opel Corsa", "Zuria")
kotxea.abiarazi()
print(kotxea.info())