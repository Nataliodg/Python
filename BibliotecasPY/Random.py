#Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron.
# Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.

#Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio entre 1 y 6.
# Como la generación de valores aleatorios es un tema muy frecuente la biblioteca estándar de Python incluye un módulo que nos resuelve la generación de valores aleatorios.

import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
print('Primer dado:',dado1)
print('Segundo dado:',dado2)
suma=dado1+dado2
if suma ==7:
    print('Gano!!')
else:
    print('Perdio!!')

print('***********************')

#********************************************************************
#Desarrollar un programa que cargue una lista con 10 enteros.
# Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
# Mostrar la lista por pantalla.
# Luego mezclar los elementos de la lista y volver a mostrarlo

import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista


def imprimir(lista):
    print(lista)    


def mezclar(lista):
    random.shuffle(lista)

#Función llamada shuffle que le pasamos como parámetro una lista y nos la devuelve con los elementos mezclados (pensemos esto nos podría servir si estamos desarrollando un juego de naipes y necesitamos mezclarlos)

# bloque principal

lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)

#*****************************************************************

#Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
# El operador debe tratar de adivinar el número ingresado.
# Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
# Mostrar cuando gana el jugador cuantos intentos necesitó.

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# intentos=0
# aleatorio=random.randint(1,100)
# elegido=-1

# print('Intenta adivinar el número que escogí entre 1 y 100')
# titulo_subrayado('Que empiece el juego!!')

# while(elegido!=aleatorio):
#     elegido=int(input('Ingrese el número: '))
#     if aleatorio>elegido:
#         print('Escogí un valor mayor')
#     else:
#         if aleatorio<elegido:
#             print('Escogí un valor menor')
#     intentos=intentos+1
# titulo_subrayado('Felicidades!!')
# print('Ganaste en',intentos,'intentos.')

#*****************************************************************

#Confeccionar una programa con las siguientes funciones:
# 1) Generar una lista con 4 elementos enteros aleatorios comprendidos entre 1 y 3. Agregar un quinto elemento con un 1.
# 2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
# 3) Imprimir la lista.

def load():
    list=[]
    for x in range(4):
        list.append(random.randint(1,3))
    list.append(1)
    return list

def controlFirst(list):
    while list[0]!=1:
        random.shuffle(list)

def print2(list):
    print(list)

#Bloque Principal:
print('****************')
list=load()
print2(list)
controlFirst(list)
print2(list)



