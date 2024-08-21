class Jokalaria:
  def __init__ (self, izena, zenbakia):
      self._izena = izena
      self._zenbakia = zenbakia

  @property
  def izena (self):
      return self._izena

  @izena.setter
  def izena (self, izena):
      self._izena = izena

  @property
  def zenbakia (self):
      return self.zenbakia

  @zenbakia.setter
  def zenbakia (self, zenbakia):
      self._zenbakia = zenbakia

  def toString (self):
      return self._izena + " " + str(self._zenbakia)