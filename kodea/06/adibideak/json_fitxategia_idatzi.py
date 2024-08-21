import json

fitxategia = open("testua.json", "r")
edukia = json.load(fitxategia)
fitxategia.close()

pertsonaia = { "id": 666, "izena": "Gumball" }
edukia.append(pertsonaia)

fitxategia = open("testua.json", "w")
fitxategia.write(json.dumps(edukia))
fitxategia.close()