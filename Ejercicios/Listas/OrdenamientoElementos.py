#1
#Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.

# sueldos=[]
# for x in range(5):
#     valor=int(input("Ingrese sueldo:$"))
#     sueldos.append(valor)

# print("Lista sin ordenar")
# print(sueldos)

# for x in range(4):
#     if sueldos[x]>sueldos[x+1]:
#         aux=sueldos[x]
#         sueldos[x]=sueldos[x+1]
#         sueldos[x+1]=aux

# print("Lista con el último elemento ordenado")
# print(sueldos)
#Pero con un único for no se ordena una lista.
#Solamente está ordenado el último elemento de la lista.

#***********************************************************
#2)
#Se debe crear y cargar una lista donde almacenar 5 sueldos.
#Ordenar de menor a mayor la lista.

# sueldos=[]
# for x in range(5):
#     valor=int(input("Ingrese sueldo:"))
#     sueldos.append(valor)

# print("Lista sin ordenar")
# print(sueldos)

# for k in range(4):
#     for x in range(4):
#         if sueldos[x]>sueldos[x+1]:
#             aux=sueldos[x]
#             sueldos[x]=sueldos[x+1]
#             sueldos[x+1]=aux

# print("Lista ordenada")
# print(sueldos)

#*****************************************************
#3)
#Crear una lista y almacenar los nombres de 5 países.
#Ordenar alfabéticamente la lista e imprimirla.

# paises=[]
# for x in range(5):
#     nom=input("Ingrese el nombre de pais:")
#     paises.append(nom)

# for k in range(4):
#     for x in range(4-k):
#         if paises[x]>paises[x+1]:
#             aux=paises[x]
#             paises[x]=paises[x+1]
#             paises[x+1]=aux

# print("Listado de paises")
# print(paises)

#*****************************************************
#4)
#Solicitar por teclado la cantidad de empleados que tiene la empresa.
#Crear y cargar una lista con todos los sueldos de dichos empleados.
#Imprimir la lista de sueldos ordenamos de menor a mayor.

# cantidad=int(input("Cuantos empleados tiene la empresa?"))
# sueldos=[]
# for x in range(cantidad):
#     su=int(input("Ingrese sueldo:"))
#     sueldos.append(su)

# # ordenamos la lista
# for k in range(cantidad-1):
#     for x in range(cantidad-1-k):
#         if sueldos[x]>sueldos[x+1]:
#             aux=sueldos[x]
#             sueldos[x]=sueldos[x+1]
#             sueldos[x+1]=aux

# print("Lista de sueldos ordenados")
# print(sueldos)

#*****************************************************
#5)
#Cargar una lista con 5 elementos enteros.
#Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

# ordenamos de menor a mayor
for k in range(4):
    for x in range(4-k):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print("Lista ordenada de menor a mayor")
print(lista)

# ordenamos de mayor a menor
for k in range(4):
    for x in range(4-k):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print("Lista ordenada de mayor a menor")
print(lista)



