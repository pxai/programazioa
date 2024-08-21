import random

zenbakiak = [4, 7, -3, 7, 1, 11, 9, 0, 5, 8]

print(zenbakiak)

for i in range(len(zenbakiak)):
    ausazko_indizea = random.randint(0, len(zenbakiak) - 1)
    aurrekoa = zenbakiak[i]
    zenbakiak[i] = zenbakiak[ausazko_indizea]
    zenbakiak[ausazko_indizea] = aurrekoa

print(zenbakiak)