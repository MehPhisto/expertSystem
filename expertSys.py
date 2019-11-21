faits = {
    "rouge": ["fraise", "tomate", "pomme"],
    "vert": ["pomme", "poire", "banane", "tomate"],
    "jaune": ["banane", "tomate", "pomme", "pêche"],
    "orange": ["mandarine", "kaki", "grenade", "pêche"],
    "pépin": ["mandarine", "pomme"],
    "noyau": ["kaki", "pêche"]
}
fruits = ["banane", "fraise", "mandarine", "pêche", "kaki", "pomme", "poire", "grenade", "tomate"]
found = False

def askQuestion(item):
    answer = ''
    if item == "rouge" or item == "vert" or item == "jaune" or item == "orange":
        answer = str(input("Votre fruit peut avoir la couleur " + str(item) + "? [o/n]"))
    else:
        answer = str(input("Votre fruit possède-t-il un ou plusieurs " + str(item) + "? [o/n]"))

    return answer

def findLowestIntersecKey(items, e):
    lowestInter = []
    lowestInterKey = 0
    for i in range(len(e) - 1):
        inter = [value for value in items if value in faits[e[i]]]
        if i == 0:
            lowestInter = inter

        if len(inter) < len(lowestInter) and i > 0:
            lowestInter = inter
            lowestInterKey = i

    return lowestInterKey

ensembles = [*faits]
possible = []

for sublist in list(faits.values()):
    for item in sublist:
        if item not in possible:
            possible.append(item)

while not found:
    print(possible)
    answ = askQuestion(ensembles[0])

    if answ == 'o':
        poss = faits[ensembles[0]]
        notPoss = []

        for item in possible:
            if item not in poss:
                notPoss.append(item)

        for item in notPoss:
            possible.remove(item)

        del faits[ensembles[0]]
        del ensembles[0]

        nextKeyToAsk = findLowestIntersecKey(ensembles[1::], ensembles) + 1
        if len(ensembles) > 1:
            tmp = ensembles[0]
            ensembles[0] = ensembles[nextKeyToAsk]
            ensembles[nextKeyToAsk] = tmp
    else:
        values = faits[ensembles[0]]
        del faits[ensembles[0]]
        del ensembles[0]
        for item in values:
            # occurences = sum(1 for value in faits.values() if item in value)
            if item in possible: # and occurences == 0:
                possible.remove(item)


    if len(possible) == 1:
        print('JE PENSE............')
        print(possible[0])
        found = True
        break

    if len(ensembles) == 0:
        print('JE N\'AI MALHEUREUSEMENT PAS TROUVE')
        break