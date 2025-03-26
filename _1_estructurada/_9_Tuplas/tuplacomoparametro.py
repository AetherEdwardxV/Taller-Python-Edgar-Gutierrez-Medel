def calcular_area(rectangulo: tuple[int, int]) -> int:
    largo, ancho = rectangulo  # rectangulo[0] = "largo"  rectangulo[1] = "ancho"
    return ancho * largo

if __name__ == '__main__':
    #Funcion que recibe una tupla y la desempaqueta

    #crear tupla
    dimensiones = (10,5)

    #Llamar a la funcion con la tupla
    area = calcular_area(dimensiones)

    print(f"El area del rectangulo es {area} mts cuadrados")