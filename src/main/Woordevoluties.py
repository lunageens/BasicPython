def codeer_woord(woord, hoofdletter):
    """"
    Deze functie gebruikt de volgende codeer methode om het woord te coderen:
    1. We nemen de eerste letter van het ingegeven woord. We tellen hoeveel letters er tussen deze letter zitten en de
    ingegeven hoofdletter.
    2. We verschuiven alle andere letters van het ingegeven woord met hetzelfde aantal plaatsjes in het alfabet. Als we
    Z tegenkomen, dan herstarten we bij A.
    3. Als uitvoer, printen we voor elke letter van het ingegeven woord een lijn. De lijn start met de betreffende hoofdletter
    van het ingegeven woord aan de linkerkant. Dan komen alle letters van het alfabet die er tussen zitten in kleine letters.
    Daarna komt er in een hoofdletter de bekomen hoofdletter van het gecodeerde woord aan de linkerkant.

    Opmerkingen:
    (1) Vind hoeveel letters het alfabet verschuift door de afstand tussen de eerste letter van het woord en de hoofdletter te
    berekenen. Ord() geeft de Unicode van characters terug. De functie chr() zet die Unicode terug om in een character (letter).
    Bijvoorbeeld, ord('A') geeft 65 terug, wat de Unicode-code is voor hoofdletter A.
    Alle Unicodes vindt je op: https://towardsdatascience.com/processing-text-with-unicode-in-python-eacc226886cb (kolommen char en Dec)

    (2) De hoofdletter en kleine letter hebben steeds andere Unicodes. In principe zou je dit allemaal in dezelfde lus
    kunnen doen, maar dan is het minder duidelijk. Met de enumerate() functie kan je ook de variable 'index' meegeven.

    (3) Bij de start doe je plus 1, omdat in range(start,stop) de start meegegeven wordt, en we hebben de hoofdletter
    van start al toegevoegd aan de lijn. Bij de stop doe je dat niet, omdat in range(start,stop) de stop niet
    meegegeven wordt, en we zullen de hoofdletter van stop later apart toevoegen aan de lijn.

    (4) De afwezigheid van deze lijn is de redenen waardoor je vorig programma wel werkte bij 'FREUD' en 'C' naar 'COBRA'
    en vice versa, maar niet bij 'LAYOUT' en 'F' naar 'FUSION' en omgekeerd. In beide gevallen is de verschuiving negatief:
    de eerste letter van het ingegeven woord staat in het alfabet verder dan de ingegeven hoofdletter waarmee je het woord
    codeert. Maar enkel in het laatste geval zorgt die negatieve verschuiving ervoor dat het gecodeerde woord letters
    bevat die verder dan het begin van het alfabet liggen. Ik illustreer wat ik bedoel met een voorbeeld:
    Bij FREUD en C, is de verschuiving gelijk aan -3. Problemen zouden zich vormen als FREUD letters bevat die A, B, of C
    zijn (de eerste drie letters van het alfabet), maar dat is niet het geval.
    Daarentegen, bij LAYOUT en F, is de verschuiving gelijk aan -6. Er vormen zich problemen als het woord LAYOUT
    de eerste zes letters van het alfabet bevat. Dit is het geval bij de A: een verschuiving van -6 geeft een unicode op
    dat geen hoofdletter is. We gaan van ord('A')=65 naar ord(';')=59. Zonder deze lijn zou het gecodeerde woord
    F;SION worden. We moeten bij de 'A' terug de 'wrapping' toepassen die we ook bij 'Z' hebben gedaan om binnen het bereik
    van de hoofdletters A-Z te blijven. Door 26 op te tellen bij de unicode, zal de verschuiving terug resulteren aan
    een hoofdletter.
    De redenen dat we deze wrappings niet gebruiken voor de kleine letters, is omdat we hier die verschillende ranges
    kunnen gebruiken. Als de startletter (in kleine letters) in het alfabet vóór de stopletter komt, gebruikt u een
    directe reeks. Als de startletter echter na de stopletter komt (zoals van 'y' naar 'c'), dan splitst u de reeks op
    in twee delen: van de startletter tot 'z', en dan van 'a' tot de stopletter. Dit splitst in feite de reeks op een
    manier die 'wrapping' nabootst zonder dat u expliciet hoeft te controleren of u voorbij 'z' gaat.
    """
    verschuiving = ord(hoofdletter) - ord(woord[0])  # Hoeveel letters we verschuiven in het alfabet. (1)

    codewoord = ''
    for letter in woord:
        # We coderen elke letter van het ingegeven woord.
        unicode_codeletter = ord(letter) + verschuiving  # Bereken de nieuwe Unicode van de letter.
        if unicode_codeletter > ord('Z'):
            # Als het verder dan 'Z' gaat, begin opnieuw door totaal aantal letters in alfabet af te trekken.
            unicode_codeletter -= 26
        elif unicode_codeletter < ord('A'):
            # Als het minder dan 'A' gaat, begin opnieuw door totaal aantal letters in alfabet op te tellen. (4)
            unicode_codeletter += 26
        codewoord += chr(unicode_codeletter)  # Voeg de gecodeerde letter toe, door terug om te zetten vanuit Unicode.

    lijnen = []
    for index, letter in enumerate(woord):  # (2)
        lijn = letter  # Voeg de hoofdletter toe aan de lijn.

        start = ord(letter.lower()) + 1  # De kleine letter van het initele woord, omgezet in Unicode. (3)
        stop = ord(codewoord[index].lower())  # De kleine letter van het gecodeerde woord, omgezet in Unicode. (3)

        if start <= stop:
            # Er komt geen z in de kleine letters voor.
            for i in range(start, stop):
                lijn += chr(i)  # Voeg de omgezette kleine letters toe aan de lijn.
        else:  # Er komt wel een Z in de kleine letters voor.
            # We gebruiken twee afzonderlijke ranges om dit op te lossen.
            for i in range(start, ord('z') + 1):  # Door die +1 te doen, zorg je dat de 'z' ook in de range komt.
                lijn += chr(i)  # Voeg de omgezette kleine letters toe aan de lijn.
            for i in range(ord('a'), stop):
                lijn += chr(i)  # Voeg de omgezette kleine letters toe aan de lijn.

        lijn += codewoord[index]  # Voeg de gecodeerde hoofdletter toe aan de lijn.
        lijnen.append(lijn)  # Voeg de lijn toe aan de lijnen lijst.

    return lijnen

woord = input('Geef een woord in met enkel hoofdleters: ')
hoofdletter = input('Geef een hoofdletter in: ')
lijnen = codeer_woord(woord, hoofdletter)
[print(lijn) for lijn in lijnen]
