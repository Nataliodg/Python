# Los datos de la tupla son inmutables a diferencia de las listas que son mutables.
# Una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos.

#1)
#Definir varias tuplas e imprimir sus elementos.

tupla=(1, 2, 3)
fecha=(25, "Diciembre", 2016)
punto=(10, 2)
persona=("Rodriguez", "Pablo", 43)
print(tupla)
print(fecha)
print(punto)
print(persona)

#*****************************************************************
#2)
#Definir una tupla con tres valores enteros.
#Convertir el contenido de la tupla a tipo lista.
#Modificar la lista y luego convertir la lista en tupla.

fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista=list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)

#*****************************************************************