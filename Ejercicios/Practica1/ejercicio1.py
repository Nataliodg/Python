#1)
#multiplicar dos números sin usar el simbolo de multiplicación

# a = int(input('Ingrese el primer valor: '))
# b = int(input('Ingrese el segundo valor: '))

# resultado = 0

# for x in range(a):
#     resultado += b

# print('El resultado es:',resultado)

#2)
#ingresar nombre y apellido e imprimirlo al reves.

# nombre=input('Ingrese el nombre: ')
# apellido=input('Ingrese el apellido: ')

# reves = nombre+apellido

# print(reves[::-1])

#3)
#Escribir una función que encuentre el elemento menor def suma n definir mis modulos crear print resta

# lista = [1, 3, 4, 6, 765, 23, -7]

# menor = 'init'

# for x in lista:
#     if menor == 'init':
#         menor = x
#     else:
#         menor = x if x < menor else menor

# print('El valor menor es ', menor)

#4)
#Escribir una función que devuelva el volumen de una esfera por su radio(4/3 * pi * r **3)

# def calcularVolumen(r):
#     return 4/3 * 3.14 * r **3

# r=int(input('Ingrese el valor del radio:'))
# resultado= calcularVolumen(r)
# print('El volumen de la esfera es:',resultado)

#5)
#Escribir una función que indique si un número es par o impar:

# def esPar(n):
#     return n % 2 == 0

# n=int(input('Ingrese el número: '))

# resultado= esPar(n)
# print('El número ingresado es par?\n',resultado)

#6)
#Escribir una función que indique cuantas vocales tiene una palabra

# palabra=input('Ingrese la palabra: ')

# vocales=0

# for x in palabra:
#     y=x.lower()
#     vocales += 1 if y =='a' or y =='e' or y =='i' or y =='o' or y =='u' else 0

# print('La cantidad de vocales es:\n',vocales)

#7)
#Escribir una aplicación que reciba una cantidad infinita de números hasta
# decir 'basta', luego que devuelva la suma de los números ingresados

# lista=[]

# print('Ingrese los números y para salir escriba "basta"')

# while True:
#     valor=input('Ingrese el valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor=int(valor)
#             lista.append(valor)
#         except:
#             print('Dato inválido!')
#             exit()

# resultado=0
# for x in lista:
#     resultado += x

# print('La suma de todos los valores es:\n',resultado)

#8)
#Escribir una función que reciba nombre y apellido, y agregarlos a un archivo.

def agregarNombreArchivo(nombre, apellido):
    c= open('nombreCompleto.txt','a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()

nombre=input('Ingrese el nombre: ')
apellido=input('Ingrese el apellido: ')

agregarNombreArchivo(nombre,apellido)
