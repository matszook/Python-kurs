# Oppgave 1.9
# Be brukeren om å skrive inn to tall
tall1 = float(input("Skriv inn det første tallet: "))
tall2 = float(input("Skriv inn det andre tallet: "))

# Sjekk om det andre tallet er større enn det første
if tall2 > tall1:
    print("Det andre tallet er større enn det første.")
elif tall2 < tall1:
    print("D16et andre tallet er mindre enn det første.")
else:
    print("Tallene er like store.")