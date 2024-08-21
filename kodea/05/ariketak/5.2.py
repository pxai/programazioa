class Janaria:
    def __init__(self, izena):
        self.izena = izena


class Fruitua(Janaria):
    def __init__(self, izena, bitaminak):
        super().__init__(izena)
        self.bitaminak = bitaminak

    def info(self):
        # return f"{self.izena} {self.bitaminak}";
        return self.izena + " " + str(self.bitaminak)

postrea = Fruitua("Kiwi", ["A", "C"])
print(postrea.info())