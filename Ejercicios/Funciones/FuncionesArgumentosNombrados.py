#1)
#Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas.
#Debe mostrar su sueldo y el nombre.
#Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"hs y cobra un sueldo de $",sueldo)


# bloque principal

# calcular_sueldo("Juan",10,120)
# calcular_sueldo(costohora=12,cantidadhoras=40,nombre="Ana")
# calcular_sueldo(cantidadhoras=90,nombre="Luis",costohora=7)

#*****************************************************************
#2)
#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


# bloque principal

# lista=cargar()
# imprimir(lista)

#*****************************************************************
#3)
#Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro.
#Definir un segundo parámetro llamado termino que por defecto almacene el valor 10.
#Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
#Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tabla(numero, terminos=11):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="")
    print()
    

# bloque principal

print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)

