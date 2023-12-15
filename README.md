# Python Oefeningen voor Sam

Eerst een korte uitleg over hoe dit (en de meeste andere) Python-projecten gestructureerd zijn. Stel je voor dat ons project een boek is. Eerst een korte uitleg over hoe dit (en de meeste andere) Python-projecten gestructureerd zijn. Stel je voor dat ons project een boek is.

**README.md:**  Eerst het document waar we nu in zitten. Het README-bestand is als de samenvatting op de achterkant van een boek. Het vertelt anderen waar je project over gaat, hoe je het moet opzetten en hoe je het gebruikt. Het is het eerste wat mensen meestal lezen, zodat ze begrijpen wat je project doet en hoe ze erdoorheen kunnen navigeren. In onze README vinden we de beschrijving van de verschillende oefeningen.

**src:** : In de map 'src' vind je de code van het project. Dit is de ruggengraat van je project waar je al je belangrijkste Python codebestanden (.py) bewaart. Deze bronmap bevat twee submappen: main en test.

**main:** Een wordt altijd main genoemd, en het is het startpunt van je project. Het bevat de code die je mij hebt gevraagd om op te lossen - de oplossingen van de oefeningen.

**test:** De andere map bevat code om de oplossing in de hoofdmap te testen - de code die achter de website zit die je me liet zien toen je je opdrachten indiende. In dit geval staat er niks, maar normaal maak je je test code zelf.

**.idea:**  Dan is er ook nog een andere map genaamd '.idea', die je ook kunt negeren. Dit zijn bestanden die instellingen en configuraties bevatten voor IntelJi IDEA, wat ik gebruikte als IDE (anderen IDEs, zoals Visual Studio, PyCharm, Jupyter Notebook, ILDE, en PyDev, zullen ook dergelijke bestanden maken). De instellingen in de .idea-map helpen de IDE aan te passen aan je voorkeuren. Bijvoorbeeld, het onthoudt welke bestanden je het laatst had geopend, je kleurenschema, code-opmaakinstellingen, en andere persoonlijke voorkeuren.

Het bevat ook instellingen voor Github, wat een cloudservice voor code is. Mensen van over de hele wereld gebruiken GitHub om hun code op te slaan, te delen met anderen en samen aan projecten te werken. Om uit te leggen wat Github doet dit is slechts ter informatie - een analogie: Stel je voor dat je aan een schoolproject werkt met je vrienden. Jullie schrijven allemaal verschillende delen van het project, en je hebt een manier nodig om ieders werk te combineren. Je wilt ook zorgen dat als iemand een fout maakt, je terug kunt naar een eerdere versie. GitHub doet dit voor coderingsprojecten. Ik kan nu gewoon de link van mijn github-repository (= 'mapje') met je delen in plaats van je alle bestanden te sturen. Als je wijzigingen aanbrengt in de code, kan ik ze ook zien op mijn computer.

## 1. Spinnen en Muggen

In de natuur groeit het aantal muggen als het warm is. Spinnen kunnen muggen eten en zo helpen om de muggenpopulatie onder controle te houden.

We kunnen de toename van het aantal muggen per week afleiden aan de hand van het totaal aantal muggen in de week ervoor en de temperatuur. Als de temperatuur onder de 18 graden is, groeien muggen niet. Vanaf 40 graden gaan de eieren van muggen dood en kunnen de muggen ook niet groeien. Bij een temperatuur tussen 18 en 39 graden is de groei afhankelijk van de temperatuur volgens de formule *groeifactor = (temperatuur - 18)/21*. Het aantal nieuwe_muggen in een week is *groeifactor * aantal_muggen*. Het aantal nieuwe_muggen wordt naar beneden afgerond op een heel aantal. De kans op opgegeten te worden voor 1 mug *kans = 1 - (0.9 tot de macht aantal_spinnen)*.

Het aantal opgegeten muggen is *kans * aantal_muggen*. Een totaal van minimaal 20 opgegeten muggen resulteert in 1 nieuwe_spin, 40 opgegeten muggen in 2 nieuwe_spinnen enz.

### Opdracht

- Vraag een gebruiker om de temperatuur in graden Celsius als geheel getal in te voeren.
- Het programma stopt als de gebruiker een temperatuur ingeeft lager dan 18 graden met de boodschap "Het is nu te koud
  voor muggen"
- Het programma stopt als de gebruiker een temperatuur ingeeft die 40 graden of hoger is met de boodschap "Het is nu te
  warm voor muggen"
- Start met 100 muggen en 1 spin
- Schrijf een lus die in tijdstappen van 1 week de groei van het aantal muggen berekent gedurende 10 weken
- Bereken in iedere stap van de lus het aantal nieuwe_muggen met de groeifactor en het aantal_muggen van de vorige stap
- Bereken in iedere stap van de lus het aantal opgegeten_muggen met het aantal_muggen en aantal_spinnen van de vorige
  stap
- Bereken in iedere stap het aantal nieuwe_spinnen met het aantal opgegeten_muggen van die stap
- Druk voor iedere week de aantallen muggen en spinnen af.

### Voorbeeld

**Eerste Voorbeeld**

Invoer:
<pre>25</pre>
Uitvoer:
<pre>
week 0 100 1
week 1 124 1
week 2 153 1
week 3 189 1
week 4 234 1
week 5 289 2
week 6 331 4
week 7 328 9
week 8 237 19
week 9 112 29
week 10 43 34
</pre>


**Tweede Voorbeeld**

Invoer:
<pre>0</pre>
Uitvoer:
<pre>Het is nu te koud voor muggen.</pre>

## 2. Gene Finding

De eerste stap bij het vinden van eitwit-coderende genen in DNA, is het vinden van Open Reading Frames, ofwel openleesramen. Een Reading Frame of leesraam is een startpunt vanaf waar je het DNA in codons, 3 letters, opdeelt. Je kan beginnen van de 1e, 2e of 3e letter in de voorwaartse DNA-streng of de 1e, 2e of 3e letter op de complementaire DNA-streng. Er zijn dus 6 leesramen in totaal. Een Open Reading Frame is een startcodon gevolgd door een aantal codons en dan een stopcodon in hetzelfde leesraam. Kijken we in een stuk DNA, dan vinden we meestal meerdere overlappende ORFs in de verschillende Reading Frames, het langste ORF is meestal een valide eitwit-coderend gen, terwijl de kortere overlappende ORFs niet voor eitwitten coderen. Er zijn nog bijkomende signalen nodig om te valideren dat de langste ORF inderdaad voor een eitwit codeert, zoals een RNA polymerase bindingsplaats en een ribosoombindingsplaats. In deze opdracht kijken we alleen naar langste ORFs.

### Opdracht

Schrijf een functie lees_dna die een bestand inleest waar een DNA sequentie in zit. De DNA streng wordt in een string-variabele gezet, zonder alle witruimtes en nieuwe regels die eventueel in het bestand staan. De input voor de functie is de bestandsnaam, de output de string variabele. Je kan ervanuit gaan dat het bestand zich in de huidige directory bevindt.

Schrijf een functie reverse_complement die een string variabele als input heeft en de complementaire streng in de omgekeerde volgorde als output geeft.

Schrijf een functie vind_orfs die een lijst genereert van alle Open Reading Frames in een stuk DNA de twee richtingen. Ieder element uit de lijst is een string variabele met de DNA sequentie. Binnen deze functie roep je de functie reverse_complement aan. We vinden alleen de ORFs die beginnen met start-codon ATG en een van de drie stop-codons TAG, TAA of TGA.

Schrijf een functie langste_orf die een lijst als input heeft, zoals gegenereerd met vind_orfs en de langst of als output heeft.

Schrijf een functie transleer_orf die een orf omzet naar aminozuur-sequentie, je kan daarvoor de tabel codon_tabel.txt gebruiken. Je kan ervanuit gaan dat het bestand codon_tabel.txt zich in de huidige directory bevindt.

## 3. Woordevoluties

Woord evoluties

Als je de letters van het woord FREUD op een uniforme manier doorheen het alfabet laat evolueren dan bekome je het woord COBRA. Daarbij laten we na de letter Z terug de letter A volgen.

[Hier is een afbeelding van Sigmund Freud naast een tabel met het alfabet en de evolutie van het woord FREUD naar COBRA.]

Op dezelfde manier verkrijg je FUSION uit LAYOUT.

[Hier is een tabel die de evolutie van het woord LAYOUT naar FUSION laat zien.]

We kunnen dezelfde techniek zelfs toepassen om woorden te vertalen.

[Hier is een tabel die laat zien hoe een woord getransformeerd kan worden.]

Dit kan toch echt wel geen toeval zijn?

### Invoer

Op de eerste regel staat een woord dat enkel bestaat uit hoofdletters. Op de tweede regel staat een hoofdletter.

### Uitvoer

De evolutie van het gegeven woord naar het woord dat begint met de gegeven letter, als we de letters op een uniforme manier doorheen het alfabet laten evolueren. De letters van het gegeven woord worden aan de linkerkant onder elkaar uitgeschreven in hoofdletters. De letters van het woord dat begint met de gegeven letter en dat men bekomt na evolutie, worden aan de rechterkant onder elkaar uitgeschreven in kleine letters, waarbij na de laatste letter van het alfabet terug de eerste letter volgt.

### Voorbeeld

**Eerste Voorbeeld:**

Invoer:
<pre>
  FREUD
  C
</pre>

Uitvoer:
<pre>
  FghijklmnopqrstuvwxyzAbC
  RstuvwxyzabcdefghiJklmnO
  EfgHiJklmnopqrstuvwxyzAaB
  UvwxyzabcdefghiJklmnopqR
  DefghijKlmnopqrstuvwxyzZA
</pre>


**Tweede Voorbeeld:**

Invoer:
<pre>
  COBRA
  F
</pre>

Uitvoer:
<pre>
  CdeF
  OpqR
  BcdE
  RstU
  AbcD
</pre>
