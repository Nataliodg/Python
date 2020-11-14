#La estructura de datos tipo diccionario utiliza una clave para acceder a un valor.
#El subíndice puede ser un entero, un float, un string, una tupla etc. (en general cualquier tipo de dato inmutable)
#Podemos relacionarlo con conceptos que conocemos:

# Un diccionario tradicional que conocemos podemos utilizar un diccionario de Python para representarlo.
#La clave sería la palabra y el valor sería la definición de dicha palabra.
# Una agenda personal también la podemos representar como un diccionario.
#La fecha sería la clave y las actividades de dicha fecha sería el valor.
# Un conjunto de usuarios de un sitio web podemos almacenarlo en un diccionario.
#El nombre de usuario sería la clave y como valor podríamos almacenar su mail, clave, fechas de login etc.

#Hay muchos problemas de la realidad que se pueden representar mediante un diccionario de Python.
# Recordemos que las listas son mutables y las tuplas inmutables.
#Un diccionario es una estructura de datos mutable es decir podemos agregar elementos, modificar y borrar.

productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)

#*****************************************************************


#Claves/Valores:
product= {
    'name': 'Book',
    'Quantity': 3,
    'Price': 19.99
}

person = {
    'firstName':'Natalio',
    'lastName' : 'Di Giacomo'
}

# print(type(product))

#Obtener solo las Claves:
print(person.keys())

#Obtener todo (te lo devuelve dentro de una tupla):
print(person.items())

#También pueden ir dentro de una lista:

products = [
    {'name': 'Book', 'Price': 19.99},
    {'name': 'Laptop', 'Price': 1000}
]
print(products)
