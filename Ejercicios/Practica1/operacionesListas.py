def load():
    list=[]
    for x in range(5):
        valor=int(input('Ingrese el valor: '))
        list.append(valor)
    return list

def printMajor(list):
    may=list[0]
    for x in range (1,5):
        if list [x]>may:
            may=list[x]
    print('Mayor de la lista: ',may)

def printSuma(list):
    suma=0
    for elemento in list:
        suma=suma+elemento
    print('Suma de todos sus elementos',suma)



