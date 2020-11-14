myStr ='Hello World'
myStr2 = 'Nata'
#print(dir(myStr))#Es una guia de todo lo que se puede hacer con un string.

print(myStr.upper())#Todo a Mayúscula
print(myStr.lower())#Todo a minuscula.
print(myStr.swapcase())#Intercambia entre May por min.
print(myStr.capitalize())#Primera letra en May.

print(myStr.replace('Hello','Bye').capitalize())#Reemplaza una palabra por otra
print(myStr.count('l'))#Contar

print(myStr.startswith('Hello'))#Devuelve True o False, si empieza con ese letra/texto.
print(myStr.endswith('World'))#Devuelve True o False, si termina con esa letra/texto.

print(myStr.split())#Los separa
print(myStr.find('w'))#Devuelve la posición.

print(myStr.index('e'))#Indice
print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[3])#Imprime la posición que le indicas.

print('My name is ' + myStr2)#Con el + sumas la variable.
print(f'Mi name is {myStr2}')#Con f y {}, le indicas la letra/texto a imprimir.
print('My name is {0}'.format(myStr2))#.format(variable) y {posición}, le indicas la letra/palabra a imprimir

