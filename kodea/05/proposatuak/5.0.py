class Instrumentua:
  def __init__(self, izena, mota):
    self._izena = izena
    self._mota = mota

  def jo (self):
    print("Jotzen ", self._izena, "jotzen")

  def info (self):
    return f"{self._izena} {self._mota}"


nireGitarra = Instrumentua("Gitarra", "klasikoa")
nireGitarra.jo()
print(nireGitarra.info())