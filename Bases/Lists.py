demoList = [1, 'Hello', 1.34, True, [1,2,3]]
colors = ['red', 'blue', 'green']

numbersList =list((1,2,3,4))#Usamos una tupla para crear una lista.
print(numbersList)
print(type(numbersList))

r=list(range(1,10))#Crea una lista apartir de un rango.
print(r)

print(len(colors))#Te devuelve el rango.
print('red' in colors)#Saber si existe la letra/palabra dentro de una lista.

#Cambiar un valor por otro:
print(colors)
colors[1]='yellow'
print(colors)

#Agregar un elemento:
colors.append('violet')
print(colors)

#Agregar más de un elemento:
colors.extend(['blue', 'black'])#Siempre dentro de una tupla.
print(colors)

#Agregar un elemento en una posición:
colors.insert(1,'orange')
print(colors)
#Agregarlo ultimo:
colors.insert(len(colors),'white')
print(colors)

#Quitar un elemento:
colors.pop()#El último elemento elimina.
print(colors)
colors.pop(1)#Le indicas el indice.
print(colors)

#Quitar un elemento que se le indica:
colors.remove('violet')
print(colors)

#Ordenarlos:
colors.sort()#Alfabeticamente
print(colors)
colors.sort(reverse=True)#Inversa
print(colors)

#Contar:
print(colors.count('red'))


