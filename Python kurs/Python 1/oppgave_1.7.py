# Starter løkken
fortsett = "ja"

while fortsett.lower() == "ja":
    # Hent inn tall eller uttrykk fra brukeren
    uttrykk = input("Skriv inn tall eller regnestykke: ")
    
    # Bruk eval til å regne ut
    resultat = eval(uttrykk)
    
    # Skriv ut resultatet
    print("Resultatet er:", resultat)
    
    # Spør om brukeren vil fortsette
    fortsett = input("Vil du legge til et nytt tall/uttrykk? ")
    
print("Takk for at du brukte kalkulatoren!")