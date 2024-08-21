class IzenZuzena:
  def __init__(self, izena, abizena):
    self._izena = izena
    self._abizena = abizena

  def zuzendu (self):
    return self._zuzendu(self._izena) + " " + self._zuzendu(self._abizena)


  def _zuzendu (self, hizkiak):
    return self._lehenengo(hizkiak) + self._gainera(hizkiak)


  def _lehenengo (self, hizkiak):
    return hizkiak[0].upper()


  def _gainera (self, hizkiak):
    return hizkiak[1:len(hizkiak)].lower()


zuzentzailea = IzenZuzena("JUAN", "PÉREZ")
print(zuzentzailea.zuzendu())