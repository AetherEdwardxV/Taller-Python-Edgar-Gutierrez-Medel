def extrae(agenda:tuple):
    i:int=0
    while (i < len(agenda)):
        nombre,correo,telefono = agenda[i]
        i+=1
        yield nombre,correo,telefono


if __name__ == '__main__':
# lista de tuplas con datos personales(10 valores) y luego extraer sus valores con iteracion

    agenda =[
        ("Ana Armendiz", "AA@gmail.com","2228123234"),
        ("Brenda Barragan", "BB@gmail.com","2228123234"),
        ("Carlos Costa", "CC@gmail.com","2228123234"),
        ("Diana Dominguez", "DD@gmail.com","2228123234"),
        ("Edgar Elizondo", "EE@gmail.com","2228123234"),
        ("Fernando Fernandez", "FF@gmail.com","2228123234"),
        ("Gustavo Gonzales", "GG@gmail.com","2228123234"),
        ("Hilda Hernandez", "HH@gmail.com","2228123234"),
        ("Ivan Irlanda", "csctomasgonzales@gmail.com","2228123234"),
        ("Jesus Jaramillo", "csctomasgonzales@gmail.com","2228123234"),
    ]

    for a,b,c in extrae(agenda):
        print(a,b,c)