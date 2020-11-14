#Python nos permite redefinir los operadores matemáticos cuando planteamos una clase.
# Los métodos especiales que debemos implementar son los siguientes:

# Para el operador +:
# __add__(self,objeto2)

# Para el operador -:
# __sub__(self,objeto2)

# Para el operador *:
# __mul__(self,objeto2)

# Para el operador //:
# __floordiv__(self,objeto2)

# Para el operador /:
# __truediv__(self,objeto2)

#*****************************************************************
#1)
#Veamos con un ejemplo la sintaxis para redefinir el operador +.
# Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne la suma de los depósitos de los dos clientes que estamos sumando.

class Cliente:
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto
    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

#Bloque Principal:

# cli1=Cliente('Ana',1200)
# cli2=Cliente('Luis',1500)
# print("El total depositado por los dos clientes es")
# print(cli1+cli2)

#*****************************************************************
#2)
#Desarrollar una clase llamada Lista, que permita pasar al método __init__ una lista de valores enteros.
# Redefinir los operadores +,-,* y // con respecto a un valor entero.

class Lista:
    def __init__(self, lista):
        self.lista=lista
    def imprimir(self):
        print(self.lista)
    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva
    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva
    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva
    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]//entero)
        return nueva


# bloque principal

lista1=Lista([3,4,5])
lista1.imprimir()
print(lista1+10)
print(lista1-10)
print(lista1*10)
print(lista1//10)
