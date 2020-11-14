#1)
#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas.
#Luego ordenar las notas de mayor a menor.
#Imprimir las notas y los nombres de los alumnos.

# alumnos=[]
# notas=[]
# for x in range(5):
#     nom=input("Ingrese el nombre del alumno:")
#     alumnos.append(nom)
#     no=int(input("Ingrese la nota de dicho alumno:"))
#     notas.append(no)

# for k in range(4):
#     for x in range(4-k):
#         if notas[x]<notas[x+1]:
#             aux1=notas[x]
#             notas[x]=notas[x+1]
#             notas[x+1]=aux1
#             aux2=alumnos[x]
#             alumnos[x]=alumnos[x+1]
#             alumnos[x+1]=aux2

# print("Lista de alumnos y sus notas ordenadas de mayor a menor")
# for x in range(5):
#     print(alumnos[x],notas[x])

#*****************************************************
#2)
#Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo.
#Ordenar alfabéticamente e imprimir los resultados.
#Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.

paises=[]
habitantes=[]
for x in range(5):
    nom=input("Ingrese el nombre del pais:")
    paises.append(nom)
    cant=int(input("Cantidad de habitantes"))
    habitantes.append(cant)

# ordenamiento alfabetico
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print("Listado de paises en orden alfabetico")
for x in range(5):
     print(paises[x],habitantes[x])

# ordenamiento por cantidad de habitantes
for k in range(4):
    for x in range(4-k):
        if habitantes[x]<habitantes[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print("Listado de paises por cantidad de habitantes")
for x in range(5):
     print(paises[x],habitantes[x])