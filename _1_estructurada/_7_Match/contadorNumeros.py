import sys

if __name__ == '__main__':

    lista = [1,4,3,2,3,5,7,9,3,2,3,5,6,10,8,6,4,3,2,7,40]
    uno: int
    dos: int
    tres: int
    cuatro: int
    cinco: int
    seis: int
    siete: int
    ocho: int
    nueve: int
    diez: int
    desconocido: int
    num: int

    #print(len(lista))

    for num in lista:
        match num:
            case 1: uno =+ 1
            case 2: dos =+ 1
            case 3: tres =+ 1
            case 4: cuatro =+ 1
            case 5: cinco =+ 1
            case 6: seis =+ 1
            case 7: siete =+ 1
            case 8: ocho =+ 1
            case 9: nueve =+ 1
            case 10:diez =+ 1
            case _: desconocido =+ 1

    print(dos)
    print(tres)
    """
    sys.stdout.write(f"Se encontraron {uno}unos")
    sys.stdout.write(f"Se encontraron {dos}")
    sys.stdout.write(f"Se encontraron {tres} tres ")
    sys.stdout.write(f"Se encontraron {cuatro} cuatros ")
    sys.stdout.write(f"Se encontraron {cinco} cincos ")
    sys.stdout.write(f"Se encontraron {seis} seis ")
    sys.stdout.write(f"Se encontraron {siete} sietes ")
    sys.stdout.write(f"Se encontraron {ocho} ochos ")
    sys.stdout.write(f"Se encontraron {nueve} nueves ")
    sys.stdout.write(f"Se encontraron {diez} dieces ")
    sys.stdout.write(f"Se encontraron {desconocido} desconocidos ")
    """



