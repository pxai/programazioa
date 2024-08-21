zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0:
    print("0 baino handiagoa den zenbaki bat sartu behar duzu")
else:
    izarrak = "\n"
    for i in range(zenbakia):
        for j in range(zenbakia):
            izarrak = izarrak + "*"
            
        izarrak = izarrak + "\n"

    print(izarrak)