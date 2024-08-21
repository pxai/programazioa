zenbakiak = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]

for zenbakia in zenbakiak:
    print(zenbakia)

for i in range(len(zenbakiak)):
    zenbakiak[i] = zenbakiak[i] + 1

for zenbakia in zenbakiak:
    print(zenbakia)


# Gehiketarako alternatiba:
# zenbakiakGehitu = zenbakiak.map( zenbakia => zenbakia + 1 )