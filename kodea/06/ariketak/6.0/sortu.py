import random

def ausazkoa (max):
    return random.randint(0, max - 1)

def pasahitzaSortu (luzera):
    hizkiak = ["a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",
        "0","1","2","3","4","5","6","7","8","9",".","-","_","!","$"]
    pasahitza = ""

    for i in range(luzera):
        hizkia = hizkiak[ausazkoa(len(hizkiak))]
        pasahitza = pasahitza + hizkia

    return pasahitza