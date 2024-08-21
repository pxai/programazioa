zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0 or zenbakia % 2 != 0:
    print("0 baino handiagoa den zenbaki bikoitia sartu behar duzu")
else:
    izarrak = ""
    while zenbakia > 0:
        izarrak = izarrak + "*"
        zenbakia = zenbakia - 1

    print(izarrak)