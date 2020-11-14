#En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa, es decir listas con componente tipo tupla.

empleado=["juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)
alumno=("pedro",[7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)
print('*************************')

#*****************************************************************
#1)
#Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
#Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.

def cargar_paisespoblacion():
    paises=[]
    for x in range(5):
        nom=input("Ingresar el nombre del pais:")
        cant=int(input("Ingrese la cantidad de habitantes:"))
        paises.append((nom,cant))
    return paises


def imprimir(paises):
    print("Paises y su poblacion:")
    for x in range(len(paises)):
        print(paises[x][0],paises[x][1])


def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("Pais con mayor cantidad de habitantes:",paises[pos][0])
    

# bloque principal

# paises=cargar_paisespoblacion()
# imprimir(paises)
# pais_maspoblacion(paises)

#*****************************************************************
#2)
#Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
# El programa debe tener las siguientes funciones:
# 1)Carga de los nombres de empleados y sus últimos tres sueldos.
# 2)Imprimir el monto total cobrado por cada empleado.
# 3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.

def cargar_empleados():
    empleados=[]
    for x in range(3):
        nom=input("Ingrese el nombre del empleado:")
        su1=int(input("Primer sueldo:$"))
        su2=int(input("Segundo sueldo:$"))
        su3=int(input("Tercer sueldo:$"))
        empleados.append([nom,(su1,su2,su3)])
    return empleados


def ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos tres meses")
    for x in range(3):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],'$',total)


def ganancias_superior10000(empleados):
    print("Empleados con ingresos superiores a $10000 en los ultimos 3 meses")
    for x in range(3):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],'$',total)


# bloque principal

# empleados=cargar_empleados()
# ganancias(empleados)
# ganancias_superior10000(empleados)

#*****************************************************************
#3)
#Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
#En una lista cargar en la primer componente el nombre del candidato 
#y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos
#en dicha provincia.
#1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
#2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

def cargar_candidatos():
    candidatos=[]
    for x in range(3):
        nom=input("Ingrese el nombre del candidato:")
        cant=int(input("Los votos de cuantas provincias tiene para cargar?"))
        provincias=[]
        for z in range(cant):
            prov=input("Nombre de provincia:")
            votos=int(input("Cantidad de votos:"))
            provincias.append((prov,votos))
        candidatos.append((nom,provincias))
    return candidatos


def totalvotos_candidato(candidatos):
    for x in range(len(candidatos)):
        suma=0
        for z in range(len(candidatos[x][1])):
            suma=suma+candidatos[x][1][z][1]
        print(candidatos[x][0],suma)    
        

# bloque principal

candidatos=cargar_candidatos()
totalvotos_candidato(candidatos)

