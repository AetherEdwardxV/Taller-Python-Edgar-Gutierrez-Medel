#Python no permite sobrecarga de metodos

import statistics as mate
"""
def suma(a:int,b:int):
    print(f"la suma de {a} + {b} = {a+b}")
"""
def suma(a:int,b=None,c=None):
    if c is None:
        if b is None:
            print(f"La suma es {a}")
        else:
            print(f"la suma de {a} + {b} = {a + b}")
    else:
        print(f"la suma de {a} + {b} + {c} = {a + b + c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p = mate.mean(lista)
    print(f"El promedio es {p}")

if __name__ == '__main__':
    suma(10)
    suma(23,47)
    suma(12,255,39)

    lista2 = [1,2,3,4,5]
    promedio = promedioArreglo(lista2)
    print(promedio)
    print(lista2)

    #En Python, el paso de argumentos se realiza por referencia de objeto, y no por valor o por referencia.
    # El comportamiento de la función depende del tipo de objeto que se pase.