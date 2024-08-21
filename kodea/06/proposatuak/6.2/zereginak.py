import json

class Zereginak:
    def __init__ (self):
        fitxategia = open("zereginak.json", "r")
        self._zereginak = json.load(fitxategia)
        fitxategia.close()

    def sortu (self, id, zeregina):
        berria = { "id": id, "zeregina": zeregina };
        self._zereginak.append(berria)

    def gorde (self):
        fitxategia = open("zereginak.json", "w")
        fitxategia.write(json.dumps(self._zereginak))
        fitxategia.close()

    def ezabatu(self, id):
        self._zereginak = list(filter(lambda datua: datua["id"] != id, self._zereginak))

    def erakutsi (self):
        emaitza = ""
        for datua in self._zereginak:
            emaitza += json.dumps(datua) + "\n"

        return emaitza