numeruak = [3, 5, -4, 2, 1, 4, 0, 6, 9, 8, 3]
errepikatua = False
i = 0
j = 0

while i < len(numeruak) and not errepikatua:
    while j < len(numeruak):
        if numeruak[i] == numeruak[j]:
            errepikatua = True
            break
        j = j + 1
    i = i + 1

if errepikatua:
    print("Zenbaki bat errepikatuta dago")
else:
    print("Ez dago zenbaki errepikaturik")