import json

if __name__ == '__main__':
    #Version corta para abrir archivo json
    #Abre el archivo  JSON en modo lectura y with cierra

    with open("datos.json","r",encoding="utf-8") as archivo:
        datos = json.load(archivo) #carga el contenido del archivo


    for persona in datos["personas"]:
        print("Nombre:",persona["Nombre"])
        print("Edad:",persona["Edad"])
        print("Ciudad:",persona["Ciudad"])
        print("Estado:",persona["Estado"])