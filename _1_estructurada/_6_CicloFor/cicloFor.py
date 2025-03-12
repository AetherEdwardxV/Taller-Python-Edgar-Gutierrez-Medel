import sys

if __name__ == '__main__':
    # range(cantidad de numeros)
    # range(numero inicial, cantidad de numeros)
    # range(numero inicial, cantidad de numeros, incremento o decremento)

    for i in range(10): # 0 - 9
        print(f"{i}")

    for i in range(6,12): # 6 - 11
        print(f"{i}")

    for i in range(20,3,-3): # 20,17,14,11,8,5
        print(f"{i}")

    for j in range(1,20): 
        print(f"{j}",end=" ") # imprime sin salto de linea
    sys.stdout.write("Texto sin salto de linea")