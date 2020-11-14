#En Python tenemos tipos de datos inmutables:

# enteros
# float
# string
# tuplas
#Mutables:

# listas
# diccionarios

#Esto tiene mucha importancia cuando enviamos a una función una variable mutable.

#1)
#Confeccionar un programa que contenga las siguientes funciones:
# 1) Carga de una lista y retorno al bloque principal.
# 2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
# 3) Imprimir la lista

def cargar():
    lista=[]
    continua="s"
    while continua=="s":
        valor=int(input("Ingrese un valor:"))
        lista.append(valor)
        continua=input("Agrega otro elemento a la lista[s/n]:")
    return lista


def fijar_cero(li):
    for x in range(len(li)):
        if li[x]<10:
            li[x]=0


def imprimir(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")

# bloque principal

# lista=cargar()
# print("Lista antes de modificar")
# imprimir(lista)
# fijar_cero(lista)
# print("Lista despues de modificar")
# imprimir(lista)

#****************************************************************
#2)
#Confeccionar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 5 nombres.
# 2) Ordenar alfabéticamente la lista.
# 3) Imprimir la lista de nombres

def cargar2():
    nombres=[]
    for x in range(5):
        nom=input("Ingrese nombre:")
        nombres.append(nom)
    return nombres


def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux=nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux


def imprimir2(nombres):
    for x in range(len(nombres)):
        print(nombres[x]," ",end="")


# bloque principal

# nombres=cargar2()
# ordenar(nombres)
# imprimir2(nombres)

#*****************************************************************
#3)
#Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
# 1) Carga de contactos y su número telefónico.
# 2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
# 3) Imprimir la lista completa de contactos con sus números telefónicos.

def cargar3():
    contactos={}
    continua="s"
    while continua=="s":
        nombre=input("Ingrese el nombre del contacto:")
        telefono=input("Ingrese el numero de telefono:")
        contactos[nombre]=telefono
        continua=input("Ingresa otro contacto[s/n]?:")
    return contactos


def modificar_telefono(contactos):
    nombre=input("Ingrese el nombre de contacto a modificar el telefono: ")
    if nombre in contactos:
        telefono=input("Ingrese el nuevo numero telefonico: ")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")


def imprimir3(contactos):
    print("Listado de todos los contactos")
    for nombre in contactos:
        print('Contacto:',nombre,'Número telefonico:',contactos[nombre])


# bloque principal

# contactos=cargar3()
# modificar_telefono(contactos)
# imprimir3(contactos)

#*****************************************************************
#4)
#Crear un diccionario en Python para almacenar los datos de empleados de una empresa.
# La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
#Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.
# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar4():
    empleados={}
    continua="s"
    while continua=="s":
        legajo=int(input("Ingrese el numero de legajo:"))
        nombre=input("Ingrese el nombre del empleado:")
        profesion=input("Ingrese el nombre de la profesión:")
        sueldo=float(input("Ingrese el sueldo:$"))
        empleados[legajo]=[nombre,profesion,sueldo]
        continua=input("Ingresa los datos de otro empleado[s/n]:")
    return empleados


def imprimir4(empleados):
    print("Listado completo de empleados")
    for legajo in empleados:
        print('Legajo:',legajo,'Empleado:',empleados[legajo][0],'Profesión:',empleados[legajo][1],'Sueldo:$',empleados[legajo][2])


def modificar_sueldo(empleados):
    legajo=int(input("Ingrese el numero de legajo para buscar empleado:"))
    if legajo in empleados:
        sueldo=float(input('Ingrese nuevo sueldo:$'))
        empleados[legajo][2]=sueldo
    else:
        print("No existe un empleado con dicho numero de legajo")


def imprimir_analistas(empleados):
    print("Listado de empleados con profesión \"Analista de Sistemas\"")
    for legajo in empleados:
        if empleados[legajo][1]=="Analista de Sistemas":
            print('Legajo:',legajo,'Empleado:',empleados[legajo][0],'Sueldo:$',empleados[legajo][2])


# bloque principal

empleados=cargar4()
imprimir4(empleados)
modificar_sueldo(empleados)
imprimir4(empleados)
imprimir_analistas(empleados)


