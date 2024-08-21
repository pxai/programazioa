import random

matrizea = [([0] * 10)] * 5

print(matrizea)

for i in range(len(matrizea)):
    random.seed()
    for j in range(len(matrizea[i])):
        matrizea[i][j] = random.randint(0, 30)

print(matrizea)

for i in range(len(matrizea)):
    for j in range(len(matrizea[i])):
        if matrizea[i][j] == 15:
            print("15 aurkitu da ", i, j)