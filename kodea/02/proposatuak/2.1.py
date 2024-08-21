balioa = ""

while balioa != 0:
    balioa = input("Sartu zenbaki bat: ")
    balioa = int(balioa)
    if balioa < 0:
        break

    for i in range(balioa):
        print("Kaixo")