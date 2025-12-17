godteri = 30
brus = 20

penger = float(input("Hvor mye penger har du? "))

if penger >= godteri:
    print("Du kan kjøpe både godteri og brus.")
elif penger >= brus:
    print("Du kan kjøpe brus, men ikke godteri.")
else:
    print("Du har ikke nok penger til hverken godteri eller brus.")