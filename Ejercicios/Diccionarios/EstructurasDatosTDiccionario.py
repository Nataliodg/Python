#1)
#En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes.
#Implementar una función para mostrar cada clave y valor.

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])


# bloque principal

# paises={"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay": 3400000}
# imprimir(paises)

#*****************************************************************
#2)
#Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.
#Desarrollar además las funciones de:
# 1) Imprimir en forma completa el diccionario
# 2) Imprimir solo los artículos con precio superior a 100.

def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:$"))
        productos[nombre]=precio
    return productos

def imprimir2(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)

# bloque principal

# productos=cargar()
# imprimir2(productos)
# imprimir_mayor100(productos)

#*****************************************************************
#3)
#Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano.
#La clave es la palabra en ingles y el valor es la palabra en castellano.
#Crear las siguientes funciones:
# 1) Cargar el diccionario.
# 2) Listado completo del diccionario.
# 3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.

def cargar2():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario


def imprimir3(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,'=',diccionario[ingles])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa:",diccionario[pal])


# bloque principal

# diccionario=cargar2()
# imprimir3(diccionario)
# consulta_palabra(diccionario)

#*****************************************************************
#4)
#Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
#Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento

def cargar3():
    personas={}
    for x in range(4):
        numero=int(input("Ingrese el numero de documento:"))
        nombre=input("Ingrese el nombre:")
        personas[numero]=nombre
    return personas


def imprimir4(personas):
    print("Listado del diccionario completo")
    for numero in personas:
        print(numero, personas[numero])


def consulta_por_numero(personas):
    nro=int(input("Ingrese el numero de documento a consultar:"))
    if nro in personas:
        print("Nombre de la persona:",personas[nro])
    else:
        print("No existe una persona con dicho numero de documento")


# bloque principal

personas=cargar3()
imprimir4(personas)
consulta_por_numero(personas)
