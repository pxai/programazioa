telefonoak = {"Ada": 66555333, "Bug": 111000111}

izena = input ("Sartu izen bat:")

telefonoak [izena]

for izena in telefonoak.keys ():
  print (izena, telefonoak[izena])