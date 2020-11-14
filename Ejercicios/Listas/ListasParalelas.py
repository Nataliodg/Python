#1)
#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)

# names=[]
# age=[]
# for x in range(3):
#     nom=input('Enter the person´s name: ')#Ingrese el nombre de la persona.
#     names.append(nom)
#     ed=int(input('Enter the age of that person: '))#Ingrese la edad de esa persona.
#     age.append(ed)

# print('Name of persons of legal age')#Nombre de las personas mayores de edad.
# for x in range(3):
#     if age[x]>=18:
#         print(names[x])

#****************************************************************
#2)
#Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
#Definir dos listas paralelas.
#Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

# products=[]
# price=[]
# for x in range(3):
#     nom=input('Enter the product name:')#Ingrese el nombre del producto.
#     products.append(nom)
#     pre=int(input('Enter the price of that product:'))#Ingrese el precio de ese producto.
#     price.append(pre)

# quantity=0
# for x in range(1,3):
#     if price[x]>price[0]:
#         quantity=quantity+1

# print('Quantity of products with a price higher than the first product introduced:')#Cantidad de productos con un precio superior al primer producto ingresado.
# print(quantity)

#*********************************************************************
#3)
#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Desaprobado" si la nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la condición “Muy Bueno”.

# names=[]
# notes=[]
# for x in range(4):
#     nom=input('Enter student´s name: ')#Ingrese el nombre del estudiante.
#     names.append(nom)
#     no=int(input('Enter student grade: '))#Ingrese la calificación del estudiante.
#     notes.append(no)

# quantity=0
# for x in range(4):
#     print(names[x])
#     print(notes[x])
#     if notes[x]>=8:
#         print('Very Good')#Muy bueno.
#         quantity=quantity+1
#     else:
#         if notes[x]>4:
#             print('Good')#Bueno.
#         else:
#             print('Disapproved')#Desaprobado.

# print('The number of very good students are: ')
# print(quantity)

#***********************************************************
#4)
#Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una.
#Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista.
#Mostrar esta tercer lista.

lista1=[]
print("Carga de la primer lista")
for x in range(4):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

lista2=[]
print("Carga de la segunda lista")
for x in range(4):
    valor=int(input("Ingrese valor:"))
    lista2.append(valor)

listasuma=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    listasuma.append(suma)

print("Lista resultante:")
print(listasuma)



