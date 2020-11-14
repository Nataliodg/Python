#1)
#Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter.
#La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))


# bloque principal

# titulo_subrayado("Sistema de Administracion")
# titulo_subrayado("Ventas","-")

#*****************************************************************
#2)
#Confeccionar una función que reciba entre 2 y 5 enteros.
#La misma nos debe retornar la suma de dichos valores.
#Debe tener tres parámetros por defecto.

def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s


# bloque principal

print("La suma de 5 + 6")
print(sumar(5,6))
print("La suma de 1 + 2 + 3")
print(sumar(1,2,3))
print("La suma de 1 + 2 + 3 + 4 + 5")
x=sumar(1,2,3,4,5)
print(x)

