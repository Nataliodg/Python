#1)
#Confeccionar una clase que represente un empleado.
# Definir como atributos su nombre y su sueldo.
# En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)

class Employe:
    def __init__(self):
        self.name=input('Ingrese el nombre del empleado: ')
        self.salary=float(input('Ingrese el sueldo: $'))
    def printE(self):
        print('Nombre:',self.name)
        print('Sueldo: $',self.salary)
    def impost(self):
        if self.salary>=3000:
            print('Debe pagar impuestos')
        else:
            print('No debe pagar impuestos')

#Bloque Principal:

# empleado=Employe()
# empleado.printE()
# empleado.impost()

#*****************************************************************
#2)
#Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos:
# inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático,
# primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def printP(self):
        print('Coordenada del punto')
        print('(',self.x,',',self.y,')')
    def printQuadrant(self):
        if self.x>0 and self.y>0:
            print('Primer cuadrante.')
        else:
            if self.x<0 and self.y>0:
                print('Segundo cuadrante.')
            else:
                if self.x<0 and self.y<0:
                    print('Tercer cuadrante.')
                else:
                    if self.x>0 and self.y<0:
                        print('Cuarto cuadrante.')

#Bloque Principal
# punto1=Point(10,-2)
# punto1.printP()
# punto1.printQuadrant()

#*****************************************************************
#3)
#Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos:
# inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado),
# imprimir su perímetro y su superficie.

class Square:
    def __init__(self,lado):
        self.lado=lado
    def showPerimeter(self):
        perimetro=self.lado*4
        print('El perimetro del cuadrado es:',perimetro)
    def showSurface(self):
        superficie=self.lado*self.lado
        print('La superficie del cuadrado es:',superficie)

#Bloque Principal:

# cuadrado1=Square(12)
# cuadrado1.showPerimeter()
# cuadrado1.showSurface()

#*****************************************************************
#4)
#Implementar la clase Operaciones.
# Se deben cargar dos valores enteros por teclado en el método __init__,
# calcular su suma, resta, multiplicación y división, cada una en un método,
# imprimir dichos resultados.

class Operation:
    def __init__(self):
        self.valor1=int(input('Ingrese primer valor: '))
        self.valor2=int(input('Ingrese segundo valor: '))
    def sumar(self):
        suma=self.valor1+self.valor2
        print ('La suma es:',suma)
    def restar(self):
        resta=self.valor1-self.valor2
        print('La resta es:',resta)
    def multiplicar(self):
        producto=self.valor1*self.valor2
        print('El producto es:',producto)
    def división(self):
        dividir=self.valor1/self.valor2
        print('LA división es:',dividir)

#Bloque Principal

operacion=Operation()
operacion.sumar()
operacion.restar()
operacion.multiplicar()
operacion.división()


