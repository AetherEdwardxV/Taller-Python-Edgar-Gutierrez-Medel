if __name__ == '__main__':
    #usar una tupla como clave en un diccionario

    diccionario1 = {    #normal
        'id':'2',
        'nombre': 'Juan',
        'apellido':'Gutierrez'
    }

    diccionario2 = {
        ("id","int"):'3',
        'nombre': 'Juana',
        'apellido':'Gomez'
    }

    diccionario2 

    #agregar tupla como clave
    diccionario2[("Ana",25)] = "Estudiante"
    diccionario2[("Luis",30)] = "Ingeniero"
    diccionario2[("Carlos",40)] = "Abogado"

    #acceder a los valores del diccionario usando la tupla
    ocupacion_ana = diccionario2[("Ana",25)]
    ocupacion_luis = diccionario2[("Luis",30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")
