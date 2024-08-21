import random

def ausazkoa(max):
    return random.randint(0, max - 1)

def izenaSortu(silabak):
    bokalak = ["a", "e", "i", "o", "u"]
    konsonanteak = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
    izena = ""

    for i in range(silabak):
        konsonantea = konsonanteak[ausazkoa(len(konsonanteak))]
        bokala = bokalak[ausazkoa(len(bokalak))]
        izena = izena + konsonantea + bokala

    return izena

print(izenaSortu(3))