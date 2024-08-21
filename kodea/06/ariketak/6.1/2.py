import menu
nireMenua = menua.Menu(["Erakutsi", "Kendu", "Irten"])

nireMenua.erakutsi()

if nireMenua.aukeratu(1):
    print("1. aukera badado menuan")
else:
    print("1. aukera ez dago menu honetan")