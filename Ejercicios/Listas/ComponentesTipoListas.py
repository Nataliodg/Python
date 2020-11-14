#1)
#Crear una lista por asignación.
#La lista tiene que tener cuatro elementos.
#Cada elemento debe ser una lista de 3 enteros.
#Imprimir sus elementos accediendo de diferentes modos.

# lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# # imprimimos la lista completa
# print(lista)
# print("---------")
# # imprimimos la primer componente
# print(lista[0])
# print("---------")
# # imprimimos la primer componente de la lista contenida
# # en la primer componente de la lista principal
# print(lista[0][0])
# print("---------")
# # imprimimos con un for la lista contenida en la primer componente
# for x in range(len(lista[0])):
#     print(lista[0][x])
# print("---------")               
# # imprimimos cada elemento entero de cada lista contenida en la lista
# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         print(lista[k][x])

#*****************************************************
#2)
#Crear una lista por asignación.
#La lista tiene que tener 2 elementos.
#Cada elemento debe ser una lista de 5 enteros.
#Calcular y mostrar la suma de cada lista contenida en la lista principal.


# lista=[[1,1,1,1,1], [2,2,2,2,2]]

# suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
# print(suma1)
# suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
# print(suma2)
# print("----------")

# suma1=0
# for x in range(len(lista[0])):
#     suma1=suma1+lista[0][x]
# suma2=0
# for x in range(len(lista[1])):
#     suma2=suma2+lista[1][x]
# print(suma1)
# print(suma2)
# print("----------")

# for k in range(len(lista)):
#     suma=0
#     for x in range(len(lista[k])):
#         suma=suma+lista[k][x]
#     print(suma)

#*****************************************************
#3)
#Crear una lista por asignación.
#La lista tiene que tener 5 elementos.
#Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
#Sumar todos los valores de las listas.

# lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

# suma=0
# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         suma=suma+lista[k][x]
# print(suma)

#******************************************************
#4)
#Imprimir la lista.
#Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
#Volver a imprimir la lista.

# lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

# print(lista)

# for x in range(len(lista[0])):
#     if lista[0][x]>50:
#         lista[0][x]=0

# print(lista)

#*****************************************************
#5)Imprimir la lista.
#Luego fijar con el valor cero todos los elementos mayores a 10 contenidos en todos los elementos de la variable "lista".
#Volver a imprimir la lista.

# lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

# print(lista)

# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         if lista[k][x]>10:
#             lista[k][x]=0
            
# print(lista)    

#******************************************************
#6)
#Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee.
#Luego imprimir el último elemento de la lista principal.

lista=[["juan","ana"], ["luis"], ["pedro","carlos","maria"]]
print(lista[len(lista)-1])       
