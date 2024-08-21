import random

def ausazkoa (max):
    return random.randint(0, max)

class Txanpona:
    def bota (self):
        aldeak = ["aurpegi", "gurutze"]
        zenbakia = ausazkoa(1)

        return aldeak[zenbakia]

txanpona = Txanpona()

for i in range(10):
    print(txanpona.bota())