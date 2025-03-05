if __name__ == '__main__':
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    c = int(input("Ingrese el ultimo numero: "))

    # seleccionar linea y mover alt+shift+up alt+shift+down
    if a>b:
        if a>c:
            print(f"El mayor es {a}")
        else:
            print(f"El mayor es {c}")
    else:
        if b>c:
            print(f"El mayor es {b}")
        else:
            print(f"El mayor es {c}")

