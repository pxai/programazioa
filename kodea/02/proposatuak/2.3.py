zenbakia = input("Sartu zenbaki bat: ")
zenbakia = int(zenbakia)

if zenbakia <= 0 or zenbakia % 2 != 0:
    print("0 baino handiagoa den zenbaki bikoitia sartu behar duzu")
else:
    sekuentzia = ""
    zenbakia = zenbakia / 2
    while zenbakia > 0:
        sekuentzia  = sekuentzia + "*-"
        zenbakia = zenbakia - 1

    sekuentzia = sekuentzia + "*"

    print(sekuentzia)