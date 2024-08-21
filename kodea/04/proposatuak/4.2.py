def agurtu(momentua):
    if momentua == "goizean":
        return "Egun on"
    elif momentua == "arratsaldean":
        return "Arratsalde on"
    elif momentua == "gauean":
        return "Gabon"
    else:
        return ""

print(agurtu("arratsaldean"))

# beste bertsio bat
def agurtu2(momentua):
    return {
        "goizean": "Egun on",
        "arratsaldean": "Arratsalde on",
        "gauero": "Gabon"
    }[momentua]

print(agurtu2("arratsaldean"))