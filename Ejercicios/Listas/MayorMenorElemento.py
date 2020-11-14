#1)
#Crear y cargar una lista con 5 enteros.
# Implementar un algoritmo que identifique el mayor valor de la lista.

# list=[]
# for x in range (5):
#     value=int(input('Enter the value: '))
#     list.append(value)

# major=list[0]
# for x in range (1,5):
#     if list[x]>major:
#         major=list[x]


# print('Complete list:')
# print(list)
# print('The biggest on the list:')#El más grande de la lista.
# print(major)
# #Contamos cuantas veces se encuentra el mayor en la lista.
# quantity=0 #Cantidad.
# for x in range(5):
#     if list[x]==major:
#         quantity=quantity+1
# if quantity>1:
#     print('The largest is repeated on the list')#El más grande se repite en la lista.


#*************************************************************
#2)
#Crear y cargar una lista con 5 enteros por teclado.
#Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

# list2=[]
# for x in range(5):
#     value=int(input('Enter the value: '))
#     list2.append(value)

# minor=list2[0]#Menor.
# position=0
# for x in range (1,5):
#     if list2[x]<minor:
#         minor=list2[x]
#         position=x

# print('Complete list:') 
# print(list2)
# print('Minor on the list:')#Menor de la lista.
# print(minor)
# print('Position of the minor in the list:')#Posición del menor en la lista.
# print(position)

#3)
#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#Mostrar el nombre de persona menor en orden alfabético

names=[]
for x in range (5):
    nom=input('Enter the person´s name: ')#Ingrese el nombre de la persona.
    names.append(nom)

minorName=names[0]
for x in range(1,5):
    if names [x]<minorName:
        minorName=names[x]

print('The complete list of names entered are:')#La lista completa de nombres ingresados son.
print(names)
print('The minor name in alphabetical order is:')#El nombre menor en orden alfabético es.
print(minorName)