import json
import sys

# Definición de códigos ANSI
RESET = "\033[0m" # Restablece el color a su valor por defecto
# Colores de texto
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
# Colores de fondo
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def ext_mayoriaEdad():
    with open("ejercicio.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    for persona in datos["personas"]:
         yield (persona["id"],persona["Nombre"],persona["Edad"],persona["RFC"])

if __name__ == '__main__':

    i = 1

    for id,nombre,edad,rfc in ext_mayoriaEdad():
        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(BLUE)
            case 4:
                sys.stdout.write(YELLOW)
            case _:
                sys.stdout.write(RESET)


        print(id, nombre,edad, rfc)

        if edad < 18:
            print("Menor de edad")
        else:
            print("Mayor de edad")
        i+=1