telefonoak = {"Ada": 666555333, "Bug": 111000111}

izena = input("Sartu izena: ")
telefonoa = input("Sartu telefono zenbakia: ")

telefonoak[izena] = int(telefonoa)

for izena in telefonoak.keys():
    print(izena, telefonoak[izena])