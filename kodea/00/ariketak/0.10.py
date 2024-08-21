balioa = input("Sartu zenbaki bat: ")
balioa = int(balioa)

positiboaEtaBikoitia = (balioa >= 0) and (balioa % 2 == 0)
emaitza = not positiboaEtaBikoitia
print("Da bikoitia eta positiboa?", emaitza)