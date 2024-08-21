telefonoak = {"Ada": 666555333, "Bug": 111000111 }

izena = input("Sartu izena: ")

del telefonoak[izena]

for izena in telefonoak.keys():
    print(izena, telefonoak[izena])