#1)
#Definir una clase llamada Punto con dos atributos x e y.
# Crearle el método especial __str__ para retornar un string con el formato (x,y).

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"


# bloque principal

# punto1=Punto(10,3)
# punto2=Punto(3,4)
# print(punto1)
# print(punto2)

#*****************************************************************
#2)
#Declarar una clase llamada Familia. 
# Definir como atributos el nombre del padre, madre y una lista con los nombres de los hijos.
# Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus hijos.

class Familia:
    def __init__(self,padre,madre,hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos
    def __str__(self):
        cadena=self.padre+","+self.madre
        for hi in self.hijos:
            cadena=cadena+","+hi
        return cadena


# bloque principal

# familia1=Familia("Pablo","Ana",["Pepe","Julio"])
# familia2=Familia("Jorge","Carla")
# familia3=Familia("Luis","Maria",["marcos"])

# print(familia1)
# print(familia2)
# print(familia3)

#*****************************************************************
#3)
#Desarrollar un programa que implemente una clase llamada Jugador.
# Definir como atributos su nombre y puntaje.
# Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)

class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
    def __str__(self):
        cadena=self.nombre+"-"
        if self.puntaje<1000:
            cadena=cadena+"principiante"
        else:
            cadena=cadena+"experto"
        return cadena


# bloque principal

jugador1=Jugador("Juan",750)
jugador2=Jugador("Ana",1200)
print(jugador1)
print(jugador2)
