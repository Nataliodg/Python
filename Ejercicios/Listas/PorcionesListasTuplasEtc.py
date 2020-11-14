#El lenguaje Python nos facilita una sintaxis muy sencilla par recuperar un trozo de una lista, tupla o cadena de caracteres.
#Veremos con una serie de ejemplos como podemos rescatar uno o varios elementos de las estructuras de datos mencionadas.


# lista1=[0,1,2,3,4,5,6]
# lista2=lista1[2:5]
# print(lista2) # 2,3,4
# lista3=lista1[1:3]
# print(lista3) # 1,2
# lista4=lista1[:3]
# print(lista4) # 0,1,2
# lista5=lista1[2:]
# print(lista5) # 2,3,4,5,6
# #Para recuperar una "porción" o trozo de una lista debemos indicar en el subíndice dos valores separados por el caracter ":".
# #Del lado izquierdo indicamos a partir de que elementos queremos recuperar y del lado derecho hasta cual posición sin incluir dicho valor.

# #Por ejemplo con la sintaxis:

# lista1=[0,1,2,3,4,5,6]
# lista2=lista1[2:5]
# print(lista2) # 2,3,4

# #Estamos recuperando de la posición 2 hasta la 5 sin incluirla.

# #También es posible no indicar alguno de los dos valores:

# lista4=lista1[:3]
# print(lista4) # 0,1,2

# #Si no indicamos el primer valor estamos diciendo que queremos recuperar desde el principio de la lista hasta la posición menos uno indicada después de los dos puntos.

# #En cambio si no indicamos el valor después de los dos puntos se recupera hasta el final de la lista:

# lista5=lista1[2:]
# print(lista5) # 2,3,4,5,6

#*****************************************************************
#1)
#Confeccionar una función que le enviemos un número de mes como parámetro y nos retorne una tupla con todos los nombres de meses que faltan hasta fin de año.

def meses_faltantes(numeromes):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numeromes:]


# bloque principal

# print("Imprimir los nombres de meses que faltan hasta fin de año")
# numeromes=int(input("Ingrese el numero de mes:"))
# mesesfalta=meses_faltantes(numeromes)
# print(mesesfalta)

#*****************************************************************
#2)
#Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres primeros.
# En el bloque principal del programa definir una tupla con los nombres de meses.
# Mostrar por pantalla los primeros tres caracteres de cada mes.

def primeros_tres(cadena):
    return cadena[:3];


# bloque principal

# meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
# for x in meses:
#     print(primeros_tres(x))

#*****************************************************************
#3)
#Realizar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 10 enteros.
# 2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
# 3) Imprimir una lista.

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Cargar valor:"))
        lista.append(valor)
    return lista


def retornar_mitad(lista):
    mitad=len(lista)//2
    return lista[:mitad]


def imprimir(lista):
    print("Contenido de la lista")
    print(lista)


# bloque principal

# lista=cargar()
# lista2=retornar_mitad(lista)
# imprimir(lista)
# imprimir(lista2)

#*****************************************************************
#4)
#Cargar una cadena por teclado luego:
# 1) Imprimir los dos primeros caracteres.
# 2) Imprimir los dos últimos
# 3) Imprimir todos menos el primero y el último caracter.

# cadena=input("Ingrese una cadena de caracteres:")
# print("Los dos primeros caracteres")
# print(cadena[:2])
# print("Los dos ultimos caracteres")
# print(cadena[len(cadena)-2:])
# print("Todos los caracteres menos el primero y el ultimo")
# print(cadena[1:len(cadena)-1])

#*****************************************************************
#Ahora veremos que podemos utilizar un valor negativo para acceder a un elemento de la estructura de datos.
lista1=[0,1,2,3,4,5,6]
print(lista1[-1]) # 6
print(lista1[-2]) # 5
print('****************')
#5)
#Confeccionar una función que reciba una palabra y verifique si es capicúa (es decir que se lee igual de izquierda a derecha que de derecha a izquierda)

def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")
    

# bloque principal

# capicua("neuquen")
# capicua("casa")

#*****************************************************************
#6)
#Cargar una cadena de caracteres por teclado.
# Mostrar la cadena del final al principio utilizando subíndices negativos.

palabra=input("Ingresar una palabra:")
indice=-1
for x in range(len(palabra)):
    print(palabra[indice],end="")
    indice=indice-1
print('*************************')
#*****************************************************************
#7)
#Confeccionar un programa con las siguientes funciones:
# 1) Cargar una lista con 5 palabras.
# 2) Intercambiar la primer palabra con la última.
# 3) Imprimir la lista

def cargar2():
    palabras=[]
    for x in range(0,5):
        pal=input("Ingrese una palabra:")
        palabras.append(pal)
    return palabras


def intercambiar(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux


def imprimir2(palabras):
    print(palabras)


# bloque principal

palabras=cargar2()
imprimir2(palabras)
intercambiar(palabras)
imprimir2(palabras)



