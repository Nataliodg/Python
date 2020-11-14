#1)
#Confeccionar una aplicación que muestre una presentación en pantalla del programa.
#Solicite la carga de dos valores y nos muestre la suma.
#Mostrar finalmente un mensaje de despedida del programa.

def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


# programa principal

# mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
# carga_suma()
# mostrar_mensaje("Gracias por utilizar este programa")

#*****************************************************************
#2)
#Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos.
#La carga de los valores hacerlo por teclado.

def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)


# programa principal

# cargar()

#*****************************************************************
#3)
#Desarrollar un programa que permita ingresar el lado de un cuadrado.
#Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.

def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)


def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)


# programa principal

# cargar_dato()

#*****************************************************************
#4)
#Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
#Llamarla desde el bloque principal del programa 3 veces con string distintos.

def cantidad_vocales(cadena):
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            cant=cant+1
    print("Cantidad de vocales de la palabra",cadena,"es:",cant)


# bloque principal
# cantidad_vocales("hola")
# cantidad_vocales("administracion")
# cantidad_vocales("correr")

#*****************************************************************
#5)
#Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ordenar_imprimir(v1,v2,v3):
    if v1<v2 and v1<v3:
        if (v2<v3):
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if (v2<v3):
            if (v1<v3):
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if (v1<v2):
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)
            

def cargar2():
    num1=int(input("Ingrese primer valor:"))
    num2=int(input("Ingrese segundo valor:"))
    num3=int(input("Ingrese tercer valor:"))
    print('Los valores ordenados:')
    ordenar_imprimir(num1,num2,num3)

    
# bloque principal

cargar2()
