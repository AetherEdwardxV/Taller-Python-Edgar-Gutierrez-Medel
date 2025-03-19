if __name__ == '__main__':
    # anade un elemento al final de la lista
    lista = [1,2,3]
    lista.append(4)
    print(lista)

    #anade elementos a otra lista
    otralista =[4,5,6]
    lista.extend(otralista)
    print(lista)

    #inserta un elemento en una posicion
    lista.insert(1,4) #(indice,elemento)
    print(lista)

    #elimina el primer elemento encontrado de la lista
    lista.remove(2)
    print(lista)

    #devuelve el elemento de una posicion y lo quita de la lista
    elemento = lista.pop(1)
    print(elemento)
    print(lista)

    #devuelve el indice de la primera aparicion del elemento
    indice = lista.index(4)
    print(indice)

    #devuelve el numero de veces que aparece un elemento en una lista
    conteo = lista.count(4)
    print(conteo)

    #ordena los elementos de forma descendente
    lista.sort(reverse=True)
    print(lista)
    lista.reverse()
    print(lista)

    #ordena los elementos de forma ascendente
    lista.sort()
    print(lista)

    #elimina todos los elementos de la lista
    lista.clear()
    print(lista)

    #devuelve una copia superficial de la lista
    lista = [1, 2, 3]
    copia_lista=lista.copy()
    lista.extend(copia_lista)
    print(lista)