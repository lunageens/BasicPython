def slag(n, bezet=None):
    """
    Simuleert een slag in honkbal en verplaatst de spelers op de honken.

    :param n: De slagwaarde, wat aangeeft hoeveel honken de spelers moeten opschuiven.
    :param bezet: Een lijst of tuple die aangeeft welke honken momenteel bezet zijn. Default waarde is geen -> Optioneel.
    :return: Een tuple met twee elementen: de gescoorde punten en de bezette honken na de slag.
    """
    # ? Kwni of deze assertions echt moeten
    assert n < 5, "te veel honken"
    assert n < 0, "te weinig honken"
    assert n % 1 == 0, "het aantal honken is geen geheel getal"

    # Als er geen honken bezet zijn, beginnen we met een lege lijst.
    if bezet is None: bezet = []
    punten = 0
    # We maken een nieuwe lijst om de originele lijst niet te wijzigen.
    nieuwe_bezet = bezet.copy()

    # We verplaatsen alle spelers op de honken.
    # Tegenwijzerzin boeit niet, is maar hoe je honken 1, 2, 3, en 4 noemt.
    nieuwe_bezet = [x + n for x in nieuwe_bezet] # elke speler al in bezet was  loopt n honken vooruit.
    # Als de slagman de bal raakt (n is niet 0), voegen we hem toe aan de honken.
    if n > 0: # Bij de nulde slag kan de slagman de bal niet raken.
        nieuwe_bezet.append(n) # slagman loopt n honken vooruit.
    # We tellen de spelers die scoren (elk getal boven 3 betekent een score).
    punten += len([x for x in nieuwe_bezet if x > 3]) # hoeveel spelers aangekomen op thuisbasis deze keer
    # We sorteren de lijst zodat alleen de bezette honken overblijven (getallen 3 of lager).
    nieuwe_bezet = sorted([x for x in nieuwe_bezet if x <= 3]) # honken die bezet zijn met spelers die na deze slag
    # nog op het veld staan, we sorteren die correct.

    # De functie geeft een tuple terug met het aantal punten en de bezette honken.
    return punten, nieuwe_bezet

def inning(slagen):
    """
    Simuleert een halve (maar van een speelhelft) inning in honkbal.

    :param slagen: Een lijst of tuple van gehele getallen die de opeenvolgende slagen voorstellen in de halve inning.
    :return: Een tuple met twee waarden: de gescoorde punten en de bezette honken aan het einde van de halve inning.
    """
    punten = 0
    bezet = []
    # Voor elke slag in de lijst van slagen:
    for slag_value in slagen:
        # We gebruiken de slag-functie om de score en de bezette honken na de slag te krijgen.
        score, bezet = slag(slag_value, bezet)
        # We tellen de punten bij elkaar op.
        punten += score

    # De functie geeft een tuple terug met het totaal aantal punten en de bezette honken.
    # De laatste loop stored die waarde van de laaste bezet correct voor de laaste slag.
    return punten, bezet

# Test de functies met de voorbeelden en print de resultaten.
print(slag(2)) # Uitvoer: (0, [2])
print(slag(0, [1, 3])) # Uitvoer: (0, [1, 3])
print(slag(1, [1, 3])) # Uitvoer: (1, [1, 2])
print(slag(2, [1, 3])) # Uitvoer: (1, [2, 3])
print(slag(3, [1, 3])) # Uitvoer: (2, [3])
print(slag(4, [1, 3])) # Uitvoer: (3, [])

print(inning([0, 1, 2, 3, 4])) # Uitvoer: (4, [])
print(inning([4, 3, 2, 1, 0])) # Uitvoer: (2, [1, 3])
print(inning([1, 1, 2, 1, 0, 0, 1, 3, 0])) # Uitvoer: (5, [3])





