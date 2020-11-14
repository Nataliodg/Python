#1)
#Confeccionar una aplicación que muestre una presentación en pantalla del programa.
#Solicite la carga de dos valores y nos muestre la suma.
#Mostrar finalmente un mensaje de despedida del programa.
#Implementar estas actividades en tres funciones.

def presentacion():
    print("Programa que permite cargar dos valores por teclado.")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")


# programa principal

# presentacion()
# carga_suma()
# finalizacion()

#*****************************************************************
#2)
#Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
#Repetir la carga e impresion de la suma 5 veces.
#Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.

def carga_suma2():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def separacion():
    print("*******************************")    


# programa principal

# for x in range(5):
#     carga_suma2()
#     separacion()

#*****************************************************************
#3)
#Desarrollar un programa con dos funciones.
#La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
#LLamar desde el bloque del programa principal a ambas funciones.

def calcular_cuadrado():
    valor=int(input("Ingrese un entero:"))
    cuadrado=valor*valor
    print("El cuadrado es",cuadrado)


def calcular_producto():
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    producto=valor1*valor2
    print("El producto de los valores es:",producto)


# bloque principal

# calcular_cuadrado()
# calcular_producto()

#*****************************************************************
#4)
#Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
#Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def menor_valor():
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    valor3=int(input("Ingrese tercer valor:"))    
    print("Menor de los tres")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)
            

# bloque principal

menor_valor()
menor_valor()
