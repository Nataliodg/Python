#Esta forma de recorrer la lista es utilizada obligatoriamente cuando queremos modificar sus elementos como podría ser

lista=[2, 3, 50, 7, 9]

print(lista) # [2, 3, 50, 7, 9]

for x in range(len(lista)):
    if lista[x]<10:
        lista[x]=0

print(lista) # [0, 0, 50, 0, 0] 
print('************************')

#Ahora veremos una segunda forma de acceder a los elementos de una lista con la estructura repetitiva for sin indicar subíndices.

lista2=[2, 3, 50, 7, 9]

for elemento in lista2:
    print(elemento)
print('************************')

#La primera imprime todos los elementos juntos dentro de una lista
#La segunda imprime cada elemento de la lista por separado.

#*****************************************************************
#1)
#Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
#Luego en otras funciones:
#1) Imprimirla en forma completa.
#2) Obtener y mostrar el mayor.
#3) Mostrar la suma de todas sus componentes.
#Utilizar la nueva sintaxis de for vista en este concepto.

def cargar():
    lista=[]
    for x in range(5):
        num=int(input("Ingrese un valor:"))
        lista.append(num)
    return lista


def imprimir(lista):
    print("Lista completa:")
    for elemento in lista:
        print(elemento)


def mayor(lista):
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    print("El elemento mayor de la lista es:",may)            
        

def sumar_elementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("La suma de todos sus elementos es:",suma)


# bloque principal

# lista=cargar()
# imprimir(lista)
# mayor(lista)
# sumar_elementos(lista)

#*****************************************************************
#2)
#Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
#Implementar las funciones:
#1) Carga de empleados.
#2) Impresión de los empleados y sus sueldos.
#3) Nombre del empleado con sueldo mayor.
#4) Cantidad de empleados con sueldo menor a 1000.

def cargar2():
    empleados=[]
    for x in range(5):
        nombre=input("Nombre del empleado:")
        sueldo=int(input("Ingrese el sueldo:$"))
        empleados.append((nombre,sueldo))
    return empleados


def imprimir2(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleados:
        print(nombre,'$',sueldo)


def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es $",empleado[1])


def sueldos_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1    
    print("Cantidad de empleados con un sueldo menor a 1000 son:",cant)
    

# bloque principal

# empleados=cargar2()
# imprimir2(empleados)
# mayor_sueldo(empleados)                        
# sueldos_menor1000(empleados)

#*****************************************************************
#3)
#Definir una función que cargue una lista con palabras y la retorne.
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.

def cargar3():
    palabras=[]
    cant=int(input("Cuantas palabras quiere cargar?"))
    for x in range(cant):
        pal=input("Ingrese palabra:")
        palabras.append(pal)
    return palabras


def palabras_mas5(palabras):
    print("Palabras ingresadas con mas de 5 caracteres")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)


# bloque principal

# palabras=cargar3()
# palabras_mas5(palabras)

#******************************************************************
#4)
#Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
#Desarrollar las funciones:
#1) Cargar por teclado.
#2) Listar los productos y precios.
#3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar4():
    productos=[]
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:$"))
        productos.append((nombre,precio))
    return productos


def imprimir4(productos):
    print("Listado de productos y precios:")
    for nombre,precio in productos:
        print(nombre,'$',precio)


def imprimir_entre10y15(productos):
    print("Listado de productos que tienen un precio comprendido entre $10 y $15")
    for nombre,precio in productos:
        if precio>=10 and precio<=50:
            print(nombre,'$',precio)


# bloque principal

productos=cargar4()
imprimir4(productos)
imprimir_entre10y15(productos)




