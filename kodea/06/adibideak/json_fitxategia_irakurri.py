import json

fitxategiarea = open("testua.json", "r")
edukia = json.load(fitxategiarea)

for pertsonaia in edukia:
    print(pertsonaia["izena"])

fitxategiarea.close()