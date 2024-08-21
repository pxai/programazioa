zenbakiak = []
aukera = -1

while aukera != "4":
    print("Aukeratu")
    print("1. Elementua sartu.")
    print("2. Elementua kendu.")
    print("3. Arraia erakutsi.")
    print("4. Irten.")
    aukera = input("Sartu aukera: ")

    if aukera == "1":
        berria = int(input("Sartu zenbakia: "))
        zenbakiak.append(berria)
    elif aukera == "2":
        zenbakiak.pop()
    elif aukera == "3":
        print(zenbakiak)
    elif aukera == "4":
        print("Agurra")
    else:
        print("Aukera ezezaguna")