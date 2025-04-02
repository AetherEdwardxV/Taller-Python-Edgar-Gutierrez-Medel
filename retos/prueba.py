if __name__ == '__main__':

    clave = "libro1"
    diclib = {
        "Titulo": ["libro1","libro2","libro3"],
        "Autor": ["alan", "german", "edgar"],
        "Genero": ["terror", "comedia", "amor"],
        "Copias": [0, 1, 2],
    }

    lislib=[
        {"Titulo": "Libro1", "Autor": "alan",    "Genero": "Libro1", "Copias":0},
        {"Titulo": "Libro2", "Autor": "armando", "Genero": "Libro1", "Copias":2},
        {"Titulo": "Libro3", "Autor": "edgar",   "Genero": "Libro1", "Copias":5},
    ]

    for i in diclib.get("Titulo"):
        print(i)


    print(list(e for e in lislib if e['Titulo'] == "Libro1")[0])



