zenbaki = input("Sartu zenbaki bat: ")
zenbaki = int(zenbaki)

if zenbaki >= 0 and zenbaki % 2 == 0:
    print(zenbaki, " bikotia eta positiboa da")
elif zenbaki < 0 and zenbaki % 2 != 0:
    print(zenbaki, " bakoitia eta negatiboa da")
elif zenbaki < 0:
    print(zenbaki, " negatiboa da")
else:
    print(zenbaki, " bakoitia da")