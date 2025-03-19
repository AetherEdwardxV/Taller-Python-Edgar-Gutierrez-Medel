import statistics as mate

if __name__ == '__main__':

    numeros =[10,20,50,80,90,30,40]

    conteo = 0
    suma=0
    promedio=0

    for valor in numeros:
        suma+=valor
        conteo+=1

    promedio=suma/conteo
    print(promedio)

    #opcionmediolenta

    suma2=0
    for valor in numeros:
            suma2+=valor
    promedio= suma/len(numeros)
    print(promedio)

    promedio = mate.mean(numeros) # la funcion "mean" de la libreria "statistics" obtiene el promedio de un conjunto de dato
    print(promedio)