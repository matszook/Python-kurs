x = 10
print("Før funksjonen", x)

def endre_x():
    global x
    x = 20
    y = 30
    print("Inni funksjonen", x)
    print("Inni funksjonen", y)

endre_x()

print("Etter funksjonen", x)