# Otra variante en la declaración de una función en Python es la definición de una cantidad variable de parámetros.
# Para definir una cantidad variable de parámetros debemos anteceder el caracter asterísco (*) al último parámetro de la función.

#1)
#Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.

def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

# print("La suma de 1+2")
# print(sumar(1,2))
# print("La suma de 1+2+3+4")
# print(sumar(1,2,3,4))
# print("La suma de 1+2+3+4+5+6+7+8+9+10")
# print(sumar(1,2,3,4,5,6,7,8,9,10))

# Desempaquetar una lista o tupla.
#Puede ser que tengamos una función que recibe una cantidad fija de parámetros y necesitemos llamarla enviando valores que se encuentran en una lista o tupla.
#La forma más sencilla es anteceder el caracter * al nombre de la variable:

def sumar2(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar2(*li)
# print(su)

#*****************************************************************
#2)
#Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def cantidad_mayores18(edad1,*edades):
    cant=0
    if edad1>=18:
        cant=cant+1
    for x in range(len(edades)):
        if edades[x]>=18:
            cant=cant+1
    return cant


# bloque principal

print("La cantidad de personas mayores a 18 son:", cantidad_mayores18(23,6,8,19,24))

