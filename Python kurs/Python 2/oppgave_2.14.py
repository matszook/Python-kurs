total = 0

for i in range(10, 21):  # 10 til 20 inkludert
    total += i
    if total > 50:
        break  # bryt løkken når totalen overstiger 50

print("Totalen er:", total)