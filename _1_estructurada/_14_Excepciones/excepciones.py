if __name__ == '__main__':
    try:
        #Codigo que puede causar una excepcion
        numero = int(input("Introduce un numero: "))
        resultado = 10/numero
    except ValueError:
        #Manejo de la excepcion si se introduce un valor invalido
        print("Error de valor: debes introducir un valor numerico entero")
    except ZeroDivisionError:
        #Manejo de la excepcion si se intenta dividir por cero
        print("Error division por cero: debes introducir un numero distinto de cero")
    else:
        #Se ejecuta si no hubo excepciones
        print(resultado)
    finally:
        print("Final del programa")