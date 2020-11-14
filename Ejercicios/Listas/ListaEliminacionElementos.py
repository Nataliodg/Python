#1)
#Crear una lista por asignación con 5 enteros.
#Eliminar el primero, el tercero y el último de la lista.

# lista=[10, 20, 30, 40, 50]

# print(lista)

# lista.pop(0)
# lista.pop(1)
# lista.pop(2)

# print(lista)
#Al eliminar uno se guarda y se resta una posición a los demas.

#*****************************************************************
#2)
#Crear una lista y almacenar 10 enteros pedidos por teclado.
#Eliminar todos los elementos que sean iguales al número entero 5.

# lista=[]
# for x in range(10):
#     valor=int(input("Ingrese valor:"))
#     lista.append(valor)

# print(lista)

# posicion=0
# while posicion<len(lista):
#     if lista[posicion]==5:
#         lista.pop(posicion)
#     else:
#         posicion=posicion+1
    
# print(lista)     

#*****************************************************************
#otra forma de eliminar elementos de una lista usando el metodo (del):

# lista=[10, 20, 30, 40, 50]

# print(lista)

# del(lista[0])
# del(lista[1])
# del(lista[2])

# print(lista) # 20 40

#*****************************************************************
#3)
#Crear dos listas paralelas.
#En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
#Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
#Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

# empleados=[]
# sueldos=[]
# cant=int(input("Cuantos empleados tiene la empresa:"))
# for x in range(cant):
#     nom=input("Ingrese el nombre:")
#     empleados.append(nom)
#     su=int(input("Ingrese el importe del sueldo:$"))
#     sueldos.append(su)

# print("Listado completo de empleados")
# for x in range(len(sueldos)):
#     print(empleados[x],sueldos[x])

# posicion=0
# while posicion<len(sueldos):
#     if sueldos[posicion]>10000:
#         sueldos.pop(posicion)
#         empleados.pop(posicion)
#     else:
#         posicion=posicion+1

# print("Listado de empleados que cobran $10000 o menos:")
# for x in range(len(sueldos)):
#     print(empleados[x],sueldos[x])

#*****************************************************************
#4)
#Crear una lista de 5 enteros y cargarlos por teclado.
#Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista1=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

print("Lista original")
print(lista1)

lista2=[]
posicion=0
while posicion<len(lista1):
    if lista1[posicion]>=10:
        lista2.append(lista1.pop(posicion))
    else:
        posicion=posicion+1

print("Lista despues de borrar los elementos mayores o iguales a 10")
print(lista1)
print("Lista generada con los elementos mayores o iguales a 10")
print(lista2)


