#Hemos visto que para importar toda la funcionalidad de un módulo de la Biblioteca estándar de Python utilizamos la palabra clave import y seguidamente el nombre del módulo:

# import random

#Con esa sintaxis todas las funcionalidades del módulo "random" pueden ser accedidas desde nuestro módulo.


#Ahora veremos que en Python tenemos otra sintaxis para las situaciones que queremos acceder a una o pocas funcionalidades de un módulo.
# Por ejemplo si queremos acceder solo a la función randint del módulo random en Python lo podemos expresar con la siguiente sintaxis:

# from random import randint


#Utilizamos la palabra clave from y seguidamente el nombre del módulo de donde queremos importar funcionalidades del mismo. Luego indicamos la palabra clave import y la funcionalidad que queremos importar, en nuestro ejemplo la función randint.
# También cambia como utilizamos la función randint dentro de nuestro módulo:

# valor=randint(1,10)
# print(valor)


#Como vemos no le antecedemos ningún nombre de módulo y hacemos referencia directamente a la función importada.
# Si necesitamos importar más de una funcionalidad de un módulo debemos separar por comas las funcionalidades importadas:

# from random import randint,shuffle

#*****************************************************************
#1)
#Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre la raíz cuadrada del número y el valor elevado al cubo.
# Para resolver este problema utilizaremos dos funcionalidades que nos provee el módulo math de la biblioteca estándar de Python

# from math import sqrt, pow

# valor=int(input("Ingrese un valor entero:"))
# r1=sqrt(valor)
# r2=pow(valor,3)
# print("La raiz cuadrada es",r1)
# print("El cubo es",r2)

#Podemos definir un nombre distinto para una funcionalidad que importamos de otro módulo.
# Esto puede tener como objetivo que nuestro programa sea más legible o evitar que un nombre de función que importamos colisione con un nombre de función de nuestro propio módulo.
#Resolveremos el mismo problema anterior pero definiendo dos alias para las funciones sqrt y pow del módulo math.

from math import sqrt as raiz, pow as elevar

valor=int(input("Ingrese un valor entero:"))
r1=raiz(valor)
r2=elevar(valor,3)
print("La raiz cuadrada es",r1)
print("El cubo es",r2)