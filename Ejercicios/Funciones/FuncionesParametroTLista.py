#1)
#Definir por asignación una lista de enteros en el bloque principal del programa.
#Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may


def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    

# bloque principal del programa

# listavalores=[10, 56, 23, 120, 94]
# print("La lista completa es")
# print(listavalores)
# print("La suma de todos su elementos es", sumarizar(listavalores))
# print("El mayor valor de la lista es", mayor(listavalores))
# print("El menor valor de la lista es", menor(listavalores))

#****************************************************************
#2)
#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
#Implementar una función que imprima el mayor y el menor valor de la lista.

def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El valor mayor de la lista es", may)
    print("El valor menor de la lista es", men)          

                
# bloque principal

# lista=[]
# for x in range(5):
#     valor=int(input("Ingrese valor:"))
#     lista.append(valor)
# mayormenor(lista)

#*****************************************************************
#3)
#Crear una lista de enteros por asignación.
#Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
#Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)


# bloque principal

# lista=[3, 7, 8, 10, 2]
# print("Lista original:",lista)
# print("Lista multiplicando cada elemento por 3")
# multiplicar(lista,3)

#*****************************************************************
#4)
#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
#Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
#En el bloque principal iniciamos por asignación la lista de string

def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x])>len(palabras[pos]):
            pos=x
    return palabras[pos]


# bloque principal

# palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
# print('Lista:',palabras)
# print("Palabra con mas caracteres:",mascaracteres(palabras))

#*****************************************************************
#5)
#Definir una lista de enteros por asignación en el bloque principal.
#Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
#Mostrar dicho producto en el bloque principal de nuestro programa.

def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod


# bloque principal

lista=[1, 2, 3, 4, 5]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",producto(lista))



