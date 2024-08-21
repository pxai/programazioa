import zerrenda

nire_zerrenda = zerrenda.Zerrenda("6.1.json")

badaude = nire_zerrenda.existitzenDa("eugene")
if badaude:
    print("Dago!")

nire_zerrenda.xehetu()
nire_zerrenda.inprimatu()

badaude = nire_zerrenda.existitzenDa("eugene")
if badaude:
    posizioa = nire_zerrenda.posizioa('eugene')
    print("Badago!")
    print(posizioa)