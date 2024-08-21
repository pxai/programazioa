zenbakia = input("Sartu zenbakia: ")
zenbakia = int(zenbakia)

if zenbakia >= 0 and zenbakia <= 99:
  if zenbakia == 1:
      print("Atezaina")
  elif zenbakia >= 1 and zenbakia <= 5:
      print("Defentsa")
  elif zenbakia >= 6 and zenbakia <= 8 or zenbakia == 11:
      print("Erdilari")
  elif zenbakia == 9:
      print("Aurrelari")
  else:
      print("Edozein")
else:
    print("Errorea, zenbakia ez dago 0 eta 99 artean")