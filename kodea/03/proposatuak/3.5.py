esaldia = input("Idatzi esaldi bat: ")
hitza = input("Idatzi esalditik hitz bat: ")

posizioa = esaldia.index(hitza)

if posizioa != -1:
    hasiera = esaldia[0:posizioa]
    bukaera = esaldia[posizioa + len(hitza):len(esaldia)]
    emaitza = f"{hasiera}{hitza.upper()}{bukaera}"

    print(emaitza)
else:
    print(hitza, "ez dago esaldian.")