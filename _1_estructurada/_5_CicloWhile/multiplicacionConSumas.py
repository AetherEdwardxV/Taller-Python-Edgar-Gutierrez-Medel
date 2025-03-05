if __name__ == '__main__':
    x =  int (input("Ingresa un numero: "))
    y =  int (input("Ingresa otro numero: "))

    i: int =0
    suma = 0

    while i<y:
        suma += x
        i=i+1

    print(f"El resultado de la multiplicacion es {suma}")