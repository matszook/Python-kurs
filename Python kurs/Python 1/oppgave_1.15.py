solgte_biler = int(input("Hvor mange biler har du solgt? "))

lønn = solgte_biler * 500

if solgte_biler > 70:
    lønn += 5000
    print("Gratulerer! Du får bonus på 5000 kr.")

print(f"Totalt får du {lønn} kr i lønn.")