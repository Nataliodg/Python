#1)
#Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

# va=int(input("Ingrese el valor del lado del cuafrado:"))
# superficie=retornar_superficie(va)
# print("La superficie del cuadrado es",superficie)

#*****************************************************************
#2)
#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor


# bloque principal
# valor1=int(input("Ingrese el primer valor:"))
# valor2=int(input("Ingrese el segundo valor:"))
# print('El mayor valor es: ',retornar_mayor(valor1,valor2))

#*****************************************************************
#3)
#Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene.
#En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces.
#Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def largo(cadena):
    return len(cadena)


# bloque principal

# nombre1=input("Ingrese primer nombre:")
# nombre2=input("Ingrese segundo nombre:")
# la1=largo(nombre1)
# la2=largo(nombre2)
# if la1==la2:
#     print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
# else:
#     if la1>la2:
#         print('El nombre',nombre1,"es mas largo")
#     else:
#         print('El nombre',nombre2,"es mas largo")

#*****************************************************************
#4)
#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def retornar_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)//3
    return promedio


# bloque principal

# valor1=int(input("Ingrese primer valor:"))
# valor2=int(input("Ingrese segundo valor:"))
# valor3=int(input("Ingrese tercer valor:"))
# print("Valor promedio de los tres numeros", retornar_promedio(valor1,valor2,valor3))

#*****************************************************************
#5)
#Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.

def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

# lado=int(input("Lado del cuadrado:"))
# print("El perimetro es:",retornar_perimetro(lado))

#*****************************************************************
#6)
#Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados
#En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.



def retornar_superficie2(lado1,lado2):
    superficie=lado1*lado2
    return superficie


# bloque principal

# print("Primer rectangulo")
# lado1=int(input("Ingrese lado menor del rectangulo:"))
# lado2=int(input("Ingrese lado mayor del rectangulo:"))
# print("Segundo rectangulo")
# lado3=int(input("Ingrese lado menor del rectangulo:"))
# lado4=int(input("Ingrese lado mayor del rectangulo:"))
# if retornar_superficie2(lado1,lado2)==retornar_superficie2(lado3,lado4):
#     print("Los dos rectangulos tiene la misma superficie")
# else:
#     if retornar_superficie2(lado1,lado2)>retornar_superficie2(lado3,lado4):
#         print("El primer rectangulo tiene una superficie mayor")
#     else:
#         print("El segundo rectangulo tiene una superficie mayor")

#*****************************************************************
#7)
#Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant


# bloque principal

palabra=input("Ingrese una palabra:")
print("La palabra",palabra,"tiene:",cantidad_vocal_a(palabra),"a/A")




