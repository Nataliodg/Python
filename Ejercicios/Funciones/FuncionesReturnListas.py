#1)
#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
#Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10.
#Desde el bloque principal del programa llamar a ambas funciones.

def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


# bloque principal del programa

# lista=carga_lista()
# print('La lista es:',lista)
# imprimir_mayor10(lista)

#*****************************************************************
#2)
#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
#Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
#Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def carga_lista2():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1,len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
    return [ma,me]                


# bloque principal del programa

# lista=carga_lista2()
# print('La lista es:',lista)
# rango=retornar_mayormenor(lista)
# print("Mayor elemento de la lista:",rango[0])
# print("Menor elemento de la lista:",rango[1])

#*****************************************************************
#3)
#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
#Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
#Imprimir la edad promedio de las personas.

def cargar_datos3():
    nom=[]
    ed=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nom.append(v1)
        v2=int(input("Ingrese la edad:"))
        ed.append(v2)
    return [nom,ed]


def mayores_edad(nom,ed):
    print("Nombres de personas mayores de edad:")
    for x in range(len(nom)):
        if ed[x]>=18:
            print(nom[x])


def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("Edad promedio de las personas:",promedio)
    

# bloque principal

# nombres,edades=cargar_datos3()
# mayores_edad(nombres,edades)
# promedio_edades(edades)           

#*****************************************************************
#4)
#En una empresa se almacenaron los sueldos de 10 personas.
#Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos.
#5) Mostrar todos los sueldos que están por debajo del promedio.

def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        su=int(input("Ingrese sueldo:$"))
        sueldos.append(su)
    return sueldos


def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print('$',sueldos[x])


def sueldos_mayor4000(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            cant=cant+1
    print("Cantidad de empleados con un sueldo superior a $4000:",cant)    


def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//10
    return promedio

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print("Sueldo promedio de la empresa:$",pro)
    print("Sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print('$',sueldos[x])


# bloque principal

# sueldos=cargar_sueldos()
# imprimir_sueldos(sueldos)
# sueldos_mayor4000(sueldos)
# sueldos_bajos(sueldos)

#*****************************************************************
#5)
#Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
#Definir las siguientes funciones:
#1) Cargar los nombres de articulos y sus precios.
#2) Imprimir los nombres y precios.
#3) Imprimir el nombre de artículo con un precio mayor
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

def cargar_datos4():
    articulos=[]
    precios=[]
    for x in range(5):
        ar=input("Ingrese el nombre del articulo:")
        articulos.append(ar)
        pre=int(input("Ingrese el precio de dicho articulo:$"))
        precios.append(pre)
    return [articulos,precios]


def imprimir(articulos,precios):
    print("Listado completo de articulos y sus precios")
    for x in range(len(articulos)):
        print(articulos[x],'$',precios[x])


def precio_mayor(articulos,precios):
    may=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>may:
            may=precios[x]
            pos=x
    print("Articulo con un precio mayor es :",articulos[pos],".Su precio es:$",may)


def consulta_precio(articulos,precios):
    valor=int(input("Ingrese un importe para mostrar los articulos con un precio menor:$"))
    for x in range(len(precios)):
        if precios[x]<valor:
            print(articulos[x],'$',precios[x])


# bloque principal

# articulos,precios=cargar_datos4()
# imprimir(articulos,precios)
# precio_mayor(articulos,precios)
# consulta_precio(articulos,precios)

#*****************************************************************
#6)
#Confeccionar un programa que permita:
#1) Cargar una lista de 10 elementos enteros.
#2) Generar dos listas a partir de la primera.
# En una guardar los valores positivos y en otra los negativos.
#3) Imprimir las dos listas generadas.

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def generar_listas(lista):
    listanega=[]
    listaposi=[]
    for x in range(len(lista)):
        if lista[x]<0:
            listanega.append(lista[x])
        else:
            if lista[x]>0:
                listaposi.append(lista[x])
    return [listanega,listaposi]                


def imprimir2(lista):
    for x in range(len(lista)):
        print(lista[x])


# programa principal

lista=cargar()
listanega,listaposi=generar_listas(lista)
print("Lista con los valores negativos")
imprimir2(listanega)
print("Lista con los valores positivos")
imprimir2(listaposi)


