zenbakiak = [3, 5, -4, 2, 1, 4, 0, 6, -9, 8, 3]

positiboak = 0
negatiboak = 0
hutsak = 0

for zenbakia in zenbakiak:
    if zenbakia > 0:
        positiboak = positiboak + 1
    elif zenbakia < 0:
        negatiboak = negatiboak + 1
    else:
        hutsak = hutsak + 1

print("Positiboak: ", positiboak)
print("Negatiboak: ", negatiboak)
print("Hutsak: ", hutsak)