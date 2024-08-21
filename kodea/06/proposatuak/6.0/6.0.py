import fitxategia
from datetime import date

nireFitxategia = fitxategia.Fitxategia("6.0.txt")

print("Aurreko edukia: ", nireFitxategia.irakurri())

nireFitxategia.idatzi("Eduki aldatuta!!! " + str(date.today()))
print("Edukia:", nireFitxategia.irakurri())