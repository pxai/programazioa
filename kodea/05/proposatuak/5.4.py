import random

def ausazkoa (maximoa):
    return random.randint(0, maximoa)

class Dadoa:
    def __init__(self, aldeak = 6, zeroOnartu = False):
        self._aldeak = aldeak
        self._zeroOnartu = zeroOnartu

    @property
    def aldeak (self):
        return self._aldeak

    @aldeak.setter
    def aldeak (self, aldeak):
        self._aldeak = aldeak

    @property
    def zeroOnartu (self):
        return self._zeroOnartu

    @zeroOnartu.setter
    def zeroOnartu (self, zeroOnartu):
        self._zeroOnartu = zeroOnartu

    def bota (self):
        zenbaki =  ausazkoa(self._aldeak)

        if not self._zeroOnartu:
            zenbaki = zenbaki + 1

        return zenbaki



dadoa = Dadoa()
for i in range(10):
    print(dadoa.bota())