import random


def ausazkoa(maximoa):
  return random.randint(0, maximoa)


def atributuakSortu(konpentsaketaMaila):
  puntuakEman = 0
  adimena = 0
  indarra = 0
  abiadura = 0

  gainontzekoPuntuak = 20
  puntuak = 0

  while gainontzekoPuntuak > 0:
    if konpentsaketaMaila > gainontzekoPuntuak:
      puntuak = gainontzekoPuntuak
      gainontzekoPuntuak = 0
    else:
      puntuak = ausazkoa(konpentsaketaMaila + 1)
      gainontzekoPuntuak = gainontzekoPuntuak - puntuak

    puntuakEman = ausazkoa(3)

    if puntuakEman == 0:
      adimena = adimena + puntuak
    elif puntuakEman == 1:
      indarra = indarra + puntuak
    elif puntuakEman == 2:
      abiadura = abiadura + puntuak

  print("\nBalioak konpentsazioaren arabera adierazita: ", konpentsaketaMaila)
  print("Adimena: ", adimena)
  print("Indarra: ", indarra)
  print("Abiadura: ", abiadura)


atributuakSortu(3)
