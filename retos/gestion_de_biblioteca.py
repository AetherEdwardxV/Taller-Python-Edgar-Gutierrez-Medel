"""
Descripcion

1.Agregar libros: Los usuarios deben poder agregar nuevos libros al sistema, especificando el título, autor, género y número de copias disponibles.
2.Buscar libros: Los usuarios deben poder buscar libros por título, autor o género.
3.Prestar libros: Los usuarios deben poder prestar libros, siempre y cuando haya copias disponibles.
4.Devolverlibros: Los usuarios deben poder devolver libros prestados.
5.Mostrar libros disponibles: Los usuarios deben poder ver una lista de todos los libros disponibles en la biblioteca.

Especificaciones:

-Utiliza listas, tuplas y diccionarios para almacenar la información de los libros.
-Implementa funciones para cada una de las operaciones del sistema.
-Utiliza argumentos opcionales y pasos de parámetros para hacer las funciones más flexibles.
-Implementa iteradores con yield para generar listas de libros de manera eficiente.
-Crea una interfaz de usuario simple en la consola para interactuar con el sistema.

Propuestas:

*Puedes usar un diccionario para almacenar la información de cada libro, donde las claves sean el título, autor, género y copias disponibles.
*Puedes usar una lista para almacenar todos los libros de la biblioteca.
*Para hacer el programa un poco mas complejo puedes implementar un sistema de usuarios donde cada usuario tenga una lista de libros prestados.
"""
def agregar_libro(lista_libros:list,titulo:str,autor:str,genero:str,copias:int):
    libro={
        "Titulo":titulo,
        "Autor":autor,
        "Genero":genero,
        "Copias":copias
    }
    lista_libros.append(libro)

def buscar_libro(lista_libros:list,categoria:str,clave:str):
    match categoria:
        case "titulo": print(list(e for e in lista_libros if e['Titulo'] == clave ))
        case "autor": print(list(e for e in lista_libros if e['Autor'] ==  clave))
        case "genero": print(list(e for e in lista_libros if e['Genero'] == clave))

def prestar_libro(libro:str,disponibles:list,prestados:list):




#def devolver_libro(libro:str,disponibles:list,prestados:list):

#def mostrar_disponibles():

if __name__ == '__main__':


    libros_disponibles = [
        {"Titulo": "Libro1", "Autor": "edgar", "Genero": "terror", "Copias": 0},
        {"Titulo": "Libro2", "Autor": "armando", "Genero": "amor", "Copias": 2},
        {"Titulo": "Libro3", "Autor": "juan", "Genero": "ciencia", "Copias": 5},
        {"Titulo": "Libro4", "Autor": "edgar", "Genero": "ficcion", "Copias": 4},
        {"Titulo": "Libro5", "Autor": "tomas", "Genero": "historia", "Copias": 2},
        {"Titulo": "Libro6", "Autor": "edgar", "Genero": "mates", "Copias": 1},
    ]

    libros_prestados = libros_disponibles.copy()

    #print(buscar_libro(libros_disponibles,"titulo","Libro2"))
    print(buscar_libro(libros_disponibles,"autor","edgar"))
    #print(libros_prestados)
    #print(prestar_libro("Libro3",libros_disponibles,libros_prestados))
    #print(libros_disponibles)
    #print(libros_prestados)
