zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0:
    print("0 baino handiagoa den zenbaki bat sartu behar duzu")
else:
    faktoriala = zenbakia
    while zenbakia > 1:
        zenbakia = zenbakia - 1
        faktoriala = faktoriala * zenbakia

    print("Emaitza: ", faktoriala)