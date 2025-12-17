# Hent timelønn og timer på samme linje
timelonn, timer = map(float, input("Skriv inn timelønn og antall timer jobbet (skilt med mellomrom): ").split())

# Finn bruttolønn
bruttolonn = timelonn * timer

# Hent skatteprosent
skatteprosent = float(input("Hvor mange prosent skatt betaler du? "))

# Regn ut skatt og nettolønn
skatt = bruttolonn * (skatteprosent / 100)
nettolonn = bruttolonn - skatt

# Skriv ut resultat
print("Bruttolønn (før skatt):", bruttolonn, "kr")
print("Skattetrekk:", skatt, "kr")
print("Nettolønn (etter skatt):", nettolonn, "kr")