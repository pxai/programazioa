import random

class Zenbakia:
    @staticmethod
    def ausazkoa (max):
      return random.randint(0, max)

for i in range(5):
  print(Zenbakia.ausazkoa(10))