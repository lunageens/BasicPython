# Bereken het aantal muggen en spinnen op basis van de temperatuur over een periode van 10 weken.

# Variablen waar je mee begint
aantal_muggen = 100
aantal_spinnen = 1
temperatuur =  int(input("Geef de temperatuur in graden Celcius als geheel getal: "))

# Check eerst: Temperatuur niet te warm of te koud?
if temperatuur < 18:
        print("Het is nu te koud voor muggen.")
elif temperatuur >= 40:
        print("Het is nu te warm voor spinnen.")
else:
    # Print resultaten Week 0
    print("week 0 " + str(aantal_muggen) + " " + str(aantal_spinnen)) #String maken van integers

    # Loop over de 10 weken
    for week in range(10): #Gaat van 0 tot 9
        #Hoeveel  nieuwe muggen deze week?
        groeifactor = (temperatuur - 18) / 21
        nieuwe_muggen = int(aantal_muggen * groeifactor) # Geeft het aantal nieuwe muggen, int doet automatisch na beneden afronden

        #Hoeveel opgegeten muggen deze week?
        kans = 1 - (0.9 ** aantal_spinnen) # Tot de macht wordt geschreven als ** in Pyton
        opgegeten_muggen = int(kans * aantal_muggen)

        #Hoeveel nieuwe spinnen deze week?
        nieuwe_spinnen = int(opgegeten_muggen / 20) # nu moeten we terug afronden naar beneden

        #Pas variableen aan voor volgende week
        aantal_muggen = aantal_muggen + nieuwe_muggen - opgegeten_muggen
        aantal_spinnen = aantal_spinnen + nieuwe_spinnen

        # Print resultaten van deze week
        weekNr = week + 1 # Gaat van 1 tot 10 nu
        print("week " + str(weekNr) + " " + str(aantal_muggen) + " " + str(aantal_spinnen)) #String maken van integers