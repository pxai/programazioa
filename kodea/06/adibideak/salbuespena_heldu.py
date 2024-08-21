balioa = input("Sartu zenbaki bat: ")

saia = True
while saia:
    try:
        balioa = int(balioa)
        karratua = balioa * balioa
        print("Karratua da: ", karratua)
        saia = False
    except:
        print("Datuak ez dira ondo konbertitu!")