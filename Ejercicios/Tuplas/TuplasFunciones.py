#1)
#Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar.
#La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.

def cargar_fecha():
    dd=int(input("Ingrese el numero de dia:"))
    mm=int(input("Ingrese el numero de mes:"))
    aa=int(input("Ingrese el numero de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")


# bloque principal

# fecha=cargar_fecha()
# imprimir_fecha(fecha)

#*****************************************************************
#2)
#Confeccionar un programa con las siguientes funciones:
# 1)Cargar una lista de 5 enteros.
# 2)Retornar el mayor y menor valor de la lista mediante una tupla.
#Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def retornar_mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    return (may,men)


# bloque principal

# lista=cargar()
# mayor,menor=retornar_mayormenor(lista)
# print("Mayor valor de la lista:",mayor)
# print("Menor valor de la lista:",menor)

#*****************************************************************
#3)
#Confeccionar un programa con las siguientes funciones:
# 1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
# 2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
#En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.

def cargar_empleado():
    nombre=input("Ingrese el nombre del empleado:")
    sueldo=float(input("Ingrese su sueldo:"))
    return (nombre,sueldo)


def mayor_sueldo(empleado1,empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0],"tiene mayor sueldo")
    else:
        print(empleado2[0],"tiene mayor sueldo")
        

# bloque principal

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)


