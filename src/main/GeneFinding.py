def lees_dna(bestandsnaam):
    """"
    Leest een DNA sequentie uit een bestand en verwijdert alle witruimtes en nieuwe regels.

    ! Let op: Gaat ervan uit dat bestand in zelfde directory zit als de code.
    """
    with open(bestandsnaam, 'r') as bestand:  # Die r staat voor read mode
        dna = bestand.read().replace('\n', '').replace(' ', '')  # Vervangen met niks
    return dna  # Een string


def reverse_complement(dna):
    """
    DNA bestaat uit vier basen: adenine (A), cytosine (C), guanine (G), en thymine (T). In de complementaire DNA streng
    wordt A vervangen door T en vice versa, en C door G en vice versa. Deze functie draait ook de volgorde van de basen om,
    omdat in de biologie de complementaire streng wordt gelezen in de tegenovergestelde richting van de originele streng.
    """
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}  # Type Dictionairy, Deze letter wordt die letter
    return ''.join(complement[base] for base in reversed(dna))  # Vertrekt van laatste letter in DNA, zoekt door welke
    # letter die wordt vervangen in de dict complement en voegt het toe aan de string die we gaan returnen


def vind_orfs(dna):
    """
    Deze functie identificeert alle Open Reading Frames (ORFs) in de gegeven DNA sequentie, zowel in de voorwaarste
    (originele) als omgekeerde richting. Een ORF is een deel van een DNA sequentie die begint met een start codon
    (meestal "ATG") en eindigt met een van de drie stopcodons ("TAG", "TAA", of "TGA").
    Deze functie doorzoekt de sequentie in stukken van drie basen (codons), beginnend vanaf drie mogelijke startpunten
    (de eerste, tweede of derde base), om ORFs te vinden. Dit process wordt herhaald van de omgekeerde complementaire
    streng.

    Opmerkingen:

    (1)  We moeten rekening houden met dat indices beginnen met 0 i.p.v. 1.
    Eerste loop basispos = eerste letter: cordons vd letters 1-3, 4-6, ... -> i=0: 0-2, 3-5, ...
    Tweede loop basispos = tweede letter: cordons vd letters 2-4, 5-7, ... --> i=1: 1-3, 4-6, ...
    Derde loop basispos = derde letter: cordons vd letters 3-5, 6-8, ... --> i=2: 2-4, 5-7, ...

    (2) range(start, stop, step) geeft nummertjes van start tot stop (niet er mee in) met step.
    We beginnen met basispositie i=0/1/2, tot het einde van de onze dna sequentie (maar enkel volledige cordons mogen
    erin dus -2) en we nemen stappen van drie.
    Voorbeeld:
    We beginnen met basispos i=0. dna= 'ATC TGA AGT TCG G'.  We zoeken dan voor indices 0-2, 3-5, 6-8 en 9-11, maar niet 12.
    Stappen van drie van index 0 (inclusief) tot 14-2=12 (exclusief). range(0, 12, 3): j is begin index van elke cordon,
    in dit geval 0, 3, 6 en 9.
    Dan kijken we naar basispos i=1. dna= 'A TCG AAG TTC GG'. We zoeken dan voor indices 1-3, 4-6, 7-9 en 10-12.
    Stappen van drie van index 1 (inclusief) tot 14-2=12 (exclusief). range(1, 12, 3): j is begin index van elke cordon
    in dit geval 1, 4, 7 en 10.
    Dan kijken we naar basispos i=2. dna= 'AT CTG AAG TTC GG'. We zoeken dan voor indices 2-4, 5-7, 8-10 en 11-12.
    Stappen van drie van index 2 (inclusief) tot 14-2=12 (exclusief). range(2, 12, 3): j is begin index van elke cordon,
    in dit geval 2, 5, 8 en 11.

    (3) In ons voorbeeld, bijvoorbeeld bij i=0 en j=3.

    (4) In ons voorbeeld, krijgen we 3-5 6-8 en 9-11 (dit is TGA AGT TCG) met k=3, 6 en 9.

    (5) In ons voorbeeld, niet het geval.

    """
    orfs = []  # Lijst waar we mogelijke orfs als string in bewaren.

    # * 1. Eerst loopen we over de originele sequentie.
    for i in range(3):  # Loop over basisposities i=0, 1, 2. (1)
        for j in range(i, len(dna) - 2, 3):  # Loop over alle mogelijke startposities van cordons. (2)
            if dna[j:j + 3] == 'ATG':  # Als het cordon dat we aan het bekijken zijn momenteel de startcordon is. (3)
                for k in range(j, len(dna) - 2, 3):  # Loop over alle mogelijke startposities van corodons vanaf het startcordon. (4)
                    if dna[k:k + 3] in ['TAA', 'TAG', 'TGA']:  # Als een van die cordons een stopcordon is. (5)
                        orfs.append(dna[j:k + 3])  # Dan start je van de beginpositie van het startcordon tot de eindpositie van de stopcordon.
                        break  # Stop binnenste loop -> stop zoeken voor eindcordon met deze startpositie van dit cordon.

                # Als we geen eindcordon zijn, ga na het volgende cordon dat na het startcordon komt. (nieuwe k)
                # Als we wel een eindcordon zijn, dan voegen we de gehele Reading Frame toe en stoppen we met dit
                # startcordon en gaan we naar het volgende cordon, dat potentieel een startcordon is (zie hieronder).

        # Als we geen startcordon zijn OF wel startcodon zijn en gezocht hebben naar mogelijk eindcordons erna,
        # dan gaan we naar volgende mogelijke start cordon. (nieuwe j)

    # Als we alle cordons met deze basispositie doorlopen hebben, dan gaan we naar de volgende basispositie. (nieuwe i)

    # * 2. Nu doen we het zelfde voor de complementaire sequentie.
    reverse_dna = reverse_complement(dna)
    for i in range(3):
        for j in range(i, len(reverse_dna) - 2, 3):
            if reverse_dna[j:j + 3] == 'ATG':
                for k in range(j, len(reverse_dna) - 2, 3):
                    if reverse_dna[k:k + 3] in ['TAA', 'TAG', 'TGA']:
                        orfs.append(reverse_dna[j:k + 3])
                        break

    # * 3. Nu geven we alle gevonden ORFs terug.
    return orfs


def langste_orf(orfs):
    """
    Deze functie zoekt het langste ORF in de lijst.

    ! Let op: Deze functie houdt geen rekening met als er orfs even lang zijn. In dat geval de eerste die is gevonden
    met die lengte.

    Die key is wel iets wat je moet weten, kan ook met:
    lengths = [len(orf) for orf in orfs]
    hoogste_lengte = max(lengths)
    index_longestorf = lengths.index(hoogste_lengte)
    langste_orf = orfs[index_longestorf]
    return langste_orf
    """
    langste_orf = max(orfs, key=len)  # Zoek het langste ORF in de lijst.
    return langste_orf

def transleer_orf(orf):
    """
    Ten slotte, deze functie vertaalt een ORF naar een aminozuursequentie. Het gebruikt een codontabel (meestal
    opgeslagen in een bestand genaamd codon_tabel.txt), die aangeeft welk aminozuur overeenkomt met elk drietal basen
    (codon) in de DNA sequentie. De functie leest de ORF drie basen tegelijk en vertaalt elk codon naar het overeenkomstige
    aminozuur volgens de tabel.

    ! Let op: De implementatie van transleer_orf is afhankelijk van de structuur van het bestand codon_tabel.txt.
    De bovenstaande code gaat ervan uit dat elke regel in het bestand een codon en het corresponderende aminozuur bevat,
    gescheiden door een spatie.

    ? Heb aminozuren in een lijst gereturnd, als dat als string is moet je initieren als '' en dan =+ gebruiken
    """
    codon_tabel = {} # Maak een lege dictionary.
    with open('codon_tabel.txt', 'r') as bestand:
        for regel in bestand: # gaat door elke regels in de bestand codon_tabel.txt.
            (codon, aminozuur) = regel.split() # split de regel waar er een spatie is.
            codon_tabel[codon] = aminozuur #Directory met als key codon en als value aminozuur.

    aminozuur_seq = []
    for i in range(0, len(orf), 3): #Loop over alle cordons van de Reading Frame.
        # De laatste letter (de len(orf) ste letter heeft index len-1 , dus daarom len(orf) en niet len(orf)+1.
        aminozuur_seq.append(codon_tabel[orf[i:i + 3]]) # Deze cordon wordt als key gevonden in de dictionary codon_tabel, en de value (aminozuur) wordt toegevoegd als aan de aminzuur_seq list.
    return aminozuur_seq

# Voorbeeld van hoe ge dit zou gebruiken
dna = lees_dna('dna.txt') # Voor voorbeeld dat ik heb, zou MAK* moeten returnen
orfs = vind_orfs(dna)
orf = langste_orf(orfs)
aminozuur_seq = transleer_orf(orf)
print(aminozuur_seq)

# TODO Wat gebeurt er als er geen Reading Frames te vinden zijn?