def suma(a:int ,b:int)->int:
    return a+b

def sumaLista(Lista:list) -> int:
    return sum(Lista)


if __name__ == '__main__':

    lista1 = [1,2,3,4,5,6,7,8,9,10]
    print(f"la suma es  {suma(3,5)} ")
    print(f"La suma del arreglo es {sumaLista(lista1)}")