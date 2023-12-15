def reduceer(codewoord):
    gereduceerd = ""
    gezien = []
    for letter in codewoord:
        if letter not in gezien:
            gereduceerd += letter
            gezien.append(letter)  # Deze letter is nu gezien.
    return gereduceerd.upper()

def codeer(serienummer, codewoord):
    gereduceerd = reduceer(codewoord)  # Bevat hoofdletters in juiste volgorde
    assert len(gereduceerd) == 10, "ongeldig codewoord"

    gecodeerd = ""
    for cijfer in str(serienummer):  # Elke cijfer apart eg 98 -> 9 8
        if int(cijfer) == 0:
            gecodeerd += gereduceerd[9]  # Laatste
        else:
            gecodeerd += gereduceerd[int(cijfer) - 1]  # Cijfer 1 wordt letter op positie 0

    return gecodeerd # Zwz al in hoofdletters gezet in reduceer()

def decodeer(gecodeerd, codewoord):
    gereduceerd = reduceer(codewoord)  # Bevat hoofdletters in juiste volgorde
    assert len(gereduceerd) == 10, "ongeldig codewoord"

    serienummer = ""
    for char in  gecodeerd:  # Elke letter apart
        if char == gereduceerd[9]:
            serienummer += "0"
        else:
            serienummer += str(gereduceerd.index(char) + 1)  # Als letter op positie 1, dan index 0 maar serienummer moet 1 worden. -> +1
    return int(serienummer)

def volgende(gecodeerd, codewoord):
    # ! Hier oppassen, van het gereduceerde codewoord nemen.
    assert len(reduceer(codewoord)) == 10, "ongeldig codewoord"
    serienummer = decodeer(gecodeerd, codewoord)
    return codeer(serienummer + 1, codewoord)


# We zetten in alle functies de nummers om naar strings -> anders 1+2 wordt 3 ipv 12.
print(reduceer('HUNTSVILLEX')) #Output: HUNTSVILEX
print(reduceer('TRICHINOPHOBIA')) #Output: TRICHIOPBA
# print(reduceer('ABCDEFGHIJKLNM')) # Output: GEEN assertion error

print(codeer(29, 'HUNTSVILLEX')) #Output: UE
print(codeer(63, 'TRICHINOPHOBIA')) #Output: NI
# print(codeer(29, 'ABCDEFGHIJKLNM')) # Output: assertion error

print(decodeer('UE', 'HUNTSVILLEX')) # Output: 29
print(decodeer('NI', 'TRICHINOPHOBIA')) # Output: 63
# print(decodeer('UE', 'ABCDEFGHIJKLNM')) # Output: assertion error

print(volgende('UE', 'HUNTSVILLEX')) # Output: NX
print(volgende('NI', 'TRICHINOPHOBIA')) # Output: NC
# print(volgende('UE', 'ABCDEFGHIJKLNM')) # Output: assertion error