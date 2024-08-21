def kalkulatu (balioa1, balioa2, eragiketa):
    if eragiketa ==  "+": return balioa1 + balioa2
    elif eragiketa == "-": return balioa1 - balioa2
    elif eragiketa == "*": return balioa1 * balioa2
    elif eragiketa == "/": return balioa1 / balioa2
    else: return "Eragiketa ezezaguna"

emaitza = kalkulatu(4, 6, "*")
print(emaitza)

emaitza = kalkulatu(5, 5, "-")
print(emaitza)

emaitza = kalkulatu(4, 3, "@")
print(emaitza)