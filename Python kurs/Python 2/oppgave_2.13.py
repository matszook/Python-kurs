i = 1
while i <= 10:
    if i == 6:
        print("Hopper over 6")
        i += 1  # Viktig! Øke før vi fortsetter
        continue
    print(i)
    i += 1

print("Loop ended")