class Menu:
    def __init__ (self, aukerak):
        self._aukerak = aukerak

    def erakutsi (self):
        for i in range(len(self._aukerak)):
            print(f"{i+1} {self._aukerak[i]}")

    def hautatu (self, zenbakia):
        return zenbakia > 0 and zenbakia <= len(self._aukerak)