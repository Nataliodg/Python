#Lo más poderoso que podemos encontrar en las estructuras de datos en Python es que podemos definir elementos que sean también estructuras de datos.
# En general se dice que podemos anidar una estructura de datos dentro de otra estructura de datos.

#Hemos dicho que un diccionario consta de claves y valores para esas claves.
# Desarrollaremos problemas donde los valores para esas claves sean tuplas y o listas.

#1)
#Confeccionar un programa que permita cargar un código de producto como clave en un diccionario.
# Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
#Implementar las siguientes actividades:
# 1) Carga de datos en el diccionario.
# 2) Listado completo de productos.
# 3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
# 4) Listado de todos los productos que tengan un stock con valor cero.

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto:"))
        descripcion=input("Ingrese la descripcion:")
        precio=float(input("Ingrese el precio:$"))
        stock=int(input("Ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("Desea cargar otro producto[s/n]?")
    return productos


def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print('Codigo:',codigo,'Producto:',productos[codigo][0],'Precio:$',productos[codigo][1],'Stock:',productos[codigo][2])


def consulta(productos):
    codigo=int(input("Ingrese el codigo de articulo a consultar:"))
    if codigo in productos:
        print('Producto:',productos[codigo][0],'Precio:',productos[codigo][1],'Stock:',productos[codigo][2])
        

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print('Codigo:',codigo,'Producto:',productos[codigo][0],'Precio:$',productos[codigo][1],'Stock:',productos[codigo][2])



# bloque principal

# productos=cargar()
# imprimir(productos)
# consulta(productos)
# listado_stock_cero(productos)

#*****************************************************************
#2)
#Confeccionar una agenda.
# Utilizar un diccionario cuya clave sea la fecha.
# Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
#Implementar las siguientes funciones:
# 1) Carga de datos en la agenda.
# 2) Listado completo de la agenda.
# 3) Consulta de una fecha.

def cargar2():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=input("ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad con formato hh:mm: ")
            actividad=input("Ingrese la descripcon de la actividad:")
            lista.append((hora,actividad))
            continua2=input("Ingresa otra actividad para la misma fecha[s/n]:")
        agenda[fecha]=lista
        continua1=input("Ingresa otra fecha[s/n]:")
    return agenda


def imprimir2(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha:",fecha)
        for hora,actividad in agenda[fecha]:
            print('Hora:',hora,'Actividad:',actividad)


def consulta_fecha(agenda):
    fecha=input("Ingrese la fecha que desea consultar con formato dd/mm/aa:")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print('Hora:',hora,'Actividad:',actividad)
    else:
        print("No hay actividades agendadas para dicha fecha")


# bloque principal

# agenda=cargar2()
# imprimir2(agenda)
# consulta_fecha(agenda)

#*****************************************************************
#3)
#Se desea almacenar los datos de 3 alumnos.
# Definir un diccionario cuya clave sea el número de documento del alumno.
# Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
#Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.


def cargar3():
    alumnos={}
    for x in range(3):
        dni=int(input("Ingrese el numero de dni:"))
        listamaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese el nombre de materia que cursa:")
            nota=int(input("Ingrese la nota:"))
            listamaterias.append((materia,nota))
            continua=input("Desea cargar otra materia para dicho alumno [s/n}:")
        alumnos[dni]=listamaterias
    return alumnos


def listar(alumnos):
    for dni in alumnos:
        print("Dni del alumno:",dni)
        print("Materias que cursa y notas:")
        for materia,nota in alumnos[dni]:
            print('Materia:',materia,'Nota:',nota)


def consulta_notas(alumnos):
    dni=int(input("Ingrese el dni a consultar:"))
    if dni in alumnos:
        for materia,nota in alumnos[dni]:
            print('Materia:',materia,'Nota:',nota)


# bloque principal

alumnos=cargar3()
listar(alumnos)
consulta_notas(alumnos)
