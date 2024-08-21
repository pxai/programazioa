izenburua = ""
hitza = ""

while hitza != ".":
    hitza = input("Idatzi hitz bat: ")
    
    if hitza != "." or hitza != "":
        izenburua = izenburua + " " + hitza

print("Sortutako esaldi:", izenburua)