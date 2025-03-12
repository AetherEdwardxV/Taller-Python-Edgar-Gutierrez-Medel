if __name__ == '__main__':
    # Listas        mutables    L = []
    # Tuplas        inmutables  T = ()
    # Set           mutables    S = {}  se ordena automaticamente
    # Diccionario   mutables    L = {clave1:valor1,clave2:valor2,}

    print("____________________________________________--")
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    for elemento in lista:
        print(elemento)

    lista2 = [1200,1300,1500]

    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    nombre:str
    nombre ="Luis"
    nombre += " Gutie"
    nombre.join("Gutierrez")
    print(nombre)

    lista3 = ["Fedelobo","Pablo","Karla"]
    cadena:str=" - ".join(lista3)
    print(cadena)

    separado = cadena.split()
    for dato in separado:
        print(dato)