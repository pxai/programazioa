def positibo (balioa):
    if balioa < 0:
        return -balioa

    return balioa


def berredura (balioa1, balioa2):
    return balioa1 ** balioa2

print(positibo(-1))
print(berredura(2, 3))
print(berredura(positibo(2), positibo(4)))
berredura(positibo(-5), positibo(4))