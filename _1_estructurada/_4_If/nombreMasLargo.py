if __name__ == '__main__':
    a = str(input("Ingrese el primer nombre: "))
    b = str(input("Ingrese el segundo nombre: "))
    c = str(input("Ingrese el tercer nombre: "))

    largoA = len(a)
    largoB = len(b)
    largoC = len(c)

    mayor = int

    if largoA == largoB or largoA == largoC or largoC == largoB:
        print(f"La longitud de las cadenas coincide")



    if len(a) > len(b):
        if len(a) > len(c):
            mayor = a
        else:
            mayor = c
    else:
        if len(b)> len(c):
            mayor = b
        else:
            mayor = c

    if mayor == a:
        print(f"El nombre mayor es {a}")

    if mayor == b:
        print(f"El nombre mayor es {b}")

    if mayor == c:
        print(f"El nombre mayor es {c}")

    if a == b:
        print(f"y es igual de largo que {b}")
    if a == c:
        print(f"y es igual de largo que {c}")
    if c == b:
        print(f"y es igual de largo que {b}")



