class Fitxategia:
  def __init__(self, fitxategiIzena):
      self._fitxategiIzena = fitxategiIzena

  def irakurri(self):
      fitxategia = open(self._fitxategiIzena, "r")
      datuak = fitxategia.read()
      fitxategia.close()

      return datuak

  def idatzi(self, eduki):
      fitxategia = open(self._fitxategiIzena, "w+")
      fitxategia.write(eduki)
      fitxategia.close()