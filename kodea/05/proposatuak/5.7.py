class Janaria:
    def __init__(self, izena, pisua):
        self._izena = izena
        self._pisua = pisua

    @property
    def izena (self):
        return self._izena

    @izena.setter
    def izena (self, izena):
        self._izena = izena

    @property
    def pisua (self):
        return self._pisua

    @pisua.setter
    def pisua (self, pisua):
        self._pisua = pisua

    def toString (self):
        return f"{self._izena} {self._pisua}"


class Fruta(Janaria):
    def __init__(self, izena, pisua, bitamina):
        super().__init__(izena, pisua)
        self._bitamina = bitamina

    @property
    def bitamina (self):
        return self._bitamina

    @bitamina.setter
    def bitamina (self, bitamina):
        self._bitamina = bitamina

    def toString (self):
        return f'{super().toString()} {self._bitamina}'


class Goxokia(Janaria):
    def __init__(self, izena, pisua, kaloria):
        super().__init__(izena, pisua)
        self._kaloria = kaloria

    @property
    def kaloria (self):
        return self._kaloria

    @kaloria.setter
    def kaloria (self, kaloria):
        self._kaloria = kaloria

    def toString (self):
        return f'{super().toString()} {self._kaloria}'


class Saskia:
    def __init__(self):
        self._janariak = []

    def sartuJanaria (self, janari):
        self._janariak.append(janari)

    def pisuGuztira (self):
        guztira = 0
        for janaria in self._janariak:
            guztira += janaria.pisua

        return guztira

    def toString (self):
        informazioa = ""
        for janaria in self._janariak:
            informazioa = informazioa + janaria.toString() + "\n"

        return informazioa


txintxa = Goxokia("Bomer", 0.2, 100)
gominoa = Goxokia("Marrubia", 0.3, 210)
udarea = Fruta("Udarea", 0.1, "B")
sagarra = Fruta("Sagarra", 0.15, "A")

saskia = Saskia()
saskia.sartuJanaria(txintxa)
saskia.sartuJanaria(gominoa)
saskia.sartuJanaria(udarea)
saskia.sartuJanaria(sagarra)

print("Saskiaren edukia:", saskia.toString())
print("Pisua guztira:", saskia.pisuGuztira())