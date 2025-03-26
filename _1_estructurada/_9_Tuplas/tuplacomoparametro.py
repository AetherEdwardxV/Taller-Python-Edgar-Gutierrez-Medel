def calcular_area(rectangulo: tuple[int, int]) -> int:
    largo, ancho = rectangulo  # rectangulo[0] = "largo"  rectangulo[1] = "ancho"
    return ancho * largo

def cuadrado(rectangulo: tuple[int,int]) -> tuple[int,int]:
    largo,ancho = rectangulo
    largo = largo*largo
    ancho = ancho*ancho
    return (largo,ancho)

if __name__ == '__main__':
    #Funcion que recibe una tupla y la desempaqueta

    #crear tupla
    dimensiones = (10,5)

    #Llamar a la funcion con la tupla
    area = calcular_area(dimensiones)

    print(f"El area del rectangulo es {area} mts cuadrados")

    largo,ancho = cuadrado((5,3))

    print(f"El cuadrado del largo es {largo} y el del ancho es {ancho}")