def ciclo(vueltas:int):
    i:int=0
    while(i<vueltas):
        i+=1
        yield i
    #return i


if __name__ == '__main__':

    for valor in ciclo(20):
        print(valor)


#lista de tuplas con datos personales(10 valores) y luego extraer sus valores con iteracion