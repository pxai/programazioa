def faktura(produktuak, kantitateak, prezioak):
    faktura = "FAKTURA\n-------------------\n"
    totala = 0

    for i in range(len(produktuak)):
        faktura = faktura + produktuak[i]
        faktura = faktura + " x " + str(kantitateak[i])
        faktura = faktura + " : " + str(prezioak[i]) + "\n"

        totala = totala + (kantitateak[i] * prezioak[i])

    faktura = faktura + "\n-----------------------\n"
    faktura = faktura + "Totala: " + str(totala)

    return faktura


# Adibidea
fakturaGuztira = faktura(["Ogia","Arraultza","Irina"],[1,6,2],[1.2, 0.2, 0.8])
print(fakturaGuztira)