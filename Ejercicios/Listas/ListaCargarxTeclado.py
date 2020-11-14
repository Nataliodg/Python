#1)
#Crear y cargar una lista con los nombres de tres alumnos.
#Cada alumno tiene dos notas, almacenar las notas en una lista paralela.
#Cada componente de la lista paralela debe ser también una lista con las dos notas.
#Imprimir luego cada nombre y sus dos notas.

# nombres=[]
# notas=[]
# for x in range(3):
#     nom=input("Ingrese el nombre del alumno:")
#     nombres.append(nom)
#     no1=int(input("Ingrese la primer nota:"))
#     no2=int(input("Ingrese la segunda nota:"))
#     notas.append([no1,no2])

# for x in range(3):
#     print(nombres[x],notas[x][0],notas[x][1])

#*******************************************************
#2)
#Se tiene que cargar la siguiente información:
#·Nombres de 3 empleados
#·Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
#Confeccionar el programa para:

#a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
#b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
#c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
#d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

# nombres=[]
# sueldos=[]
# totalsueldos=[]

# for x in range(3):
#     nom=input("Ingrese el nombre del empleado:")
#     nombres.append(nom)
#     su1=int(input("Ingrese el primer sueldo:$"))
#     su2=int(input("Ingrese el segundo sueldo:$"))
#     su3=int(input("Ingrese el tercer sueldo:$"))
#     sueldos.append([su1, su2, su3])

# for x in range(3):
#     total=sueldos[x][0]+sueldos[x][1]+sueldos[x][2]
#     totalsueldos.append(total)

# for x in range(3):
#     print(nombres[x], totalsueldos[x])

# posmayor=0
# mayor=totalsueldos[0]
# for x in range(1,3):
#     if totalsueldos[x]>mayor:
#         mayor=totalsueldos[x]
#         posmayor=x
# print("Empleado con mayores ingresos en los ultimos tres meses")
# print(nombres[posmayor])
# print("con un ingreso de $",mayor)

#*******************************************************
#3)
#Solicitar por teclado dos enteros.
#El primer valor indica la cantidad de elementos que crearemos en la lista.
#El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
#Mostrar la lista y la suma de todos sus elementos.

# lista=[]
# elementos=int(input("Cuantos elementos tendra la lista:"))
# sub=int(input("Cuantos elementos tendran las listas internas:"))
# for k in range(elementos):
#     lista.append([])
#     for x in range(sub):
#         valor=int(input("Ingrese valor:"))
#         lista[k].append(valor)

# print(lista)

# suma=0
# for k in range(len(lista)):
#     for x in range(len(lista[k])):
#         suma=suma+lista[k][x]

# print("La suma de todos sus elementos:",suma) 

#*******************************************************
#4)
#Definir dos listas de 3 elementos.
#La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
#La segunda lista está constituida por listas con los nombres de los hijos de cada familia.
#Puede haber familias sin hijos.
#Imprimir los nombres del padre, la madre y sus hijos.
#También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

# padres=[]
# hijos=[]
# for k in range(3):
#     pa=input("Ingrese el nombre del padre:")
#     ma=input("Ingrese el nombre de la madre:")    
#     padres.append([pa, ma])
#     cant=int(input("Cuantos hijos tienen esta familia:"))
#     hijos.append([])
#     for x in range(cant):
#         nom=input("Ingrese el nombre del hijo:")
#         hijos[k].append(nom)

# print("Listado del padre, madre y sus hijos")
# for k in range(3):
#     print("Padre:",padres[k][0])
#     print("Madre:",padres[k][1])
#     for x in range(len(hijos[k])):
#         print("Hijo:",hijos[k][x])

# print("Listado del padre y cantidad de hijos que tiene")
# for x in range(3):
#     print("padre:",padres[x][0])
#     print("Cantidad de hijos:",len(hijos[x]))

#*******************************************************
#5)
#Se desea saber la temperatura media trimestral de cuatro paises.
#Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
#a) - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
#b) - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
#c) - Calcular la temperatura media trimestral de cada país.
#d) - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
#e) - Imprimir el nombre del pais con la temperatura media trimestral mayor.

# paises=[]
# temperaturas=[]
# promediotemp=[]

# for x in range(4):
#     nom=input("Ingrese el nombre del pais:")
#     paises.append(nom)
#     temp1=int(input("Ingrese primer temperatura:"))
#     temp2=int(input("Ingrese segunda temperatura:"))
#     temp3=int(input("Ingrese tercer temperatura:"))
#     temperaturas.append([temp1, temp2, temp3])

# print("Paises y temperaturas medias de los ultimos tres meses mensuales")
# for x in range(4):
#     print(paises[x],temperaturas[x][0],temperaturas[x][1],temperaturas[x][2])

# for x in range(4):
#     pro=(temperaturas[x][0]+temperaturas[x][1]+temperaturas[x][2])//3
#     promediotemp.append(pro)

# print("Paises y temperaturas medias trimestrales")
# for x in range(4):
#     print(paises[x],promediotemp[x])

# posmayor=0
# for x in range(1,4):
#     if promediotemp[x]>promediotemp[posmayor]:
#         posmayor=x
# print("Pais con temperatura media trimestral mayor:", paises[posmayor])

#*****************************************************************
#6)
#Definir una lista y almacenar los nombres de 3 empleados.
#Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
#Imprimir los nombres de empleados y los días que faltó.
#Mostrar los empleados con la cantidad de inasistencias.
#Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.

# empleados=[]
# faltas=[]

# for k in range(3):
#     nom=input("Ingrese el nombre de empleado:")
#     empleados.append(nom)
#     cant=int(input("Cuantos dias falto:"))
#     faltas.append([])
#     for x in range(cant):
#         dia=int(input("Ingrese el numero de dia que falto:"))
#         faltas[k].append(dia)

# print("Nombres de empleados y dias que falto")
# for k in range(3):
#     print(empleados[k])
#     for x in range(len(faltas[k])):
#         print(faltas[k][x])

# print("Nombres de empleados y cantidad de inasistencias")
# for x in range(3):
#     print(empleados[x],len(faltas[x]))

# men=len(faltas[0])
# for x in range(1,3):
#     if len(faltas[x])<men:
#         men=len(faltas[x])

# print("Empleado o empleados que faltaron menos")
# for x in range(3):
#     if len(faltas[x])==men:
#            print(empleados[x])

#*****************************************************************
#7)
#Desarrollar un programa que cree una lista de 50 elementos.
#El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.

lista=[]
cant=1
for k in range(25):
    lista.append([])
    valor=1
    for x in range(cant):
        lista[k].append(valor)
        valor=valor+1
    cant=cant+1

print(lista)   

