#Python también nos permite redefinir los operadores relacionales cuando planteamos una clase.
# Los métodos especiales que podemos implementar son los siguientes:

# Para el operador ==:
# __eq__(self,objeto2)

# Para el operador !=:
# __ne__(self,objeto2)

# Para el operador >:
# __gt__(self,objeto2)

# Para el operador >=:
# __ge__(self,objeto2)

# Para el operador <:
# __lt__(self,objeto2)

# Para el operador <=:
# __le__(self,objeto2)

# Es importante recordar que una redefinición de un operador tiene sentido si ayuda y
# hace más claro nuestro algoritmo.

#*****************************************************************
#1)
#Crear una clase Persona que tenga como atributo el nombre y la edad.
# El operador == retornará verdadero si las dos personas tienen la misma edad,
# el operador > retornará True si la edad del objeto de la izquierda tiene una edad mayor a la edad del objeto de la derecha del operador >,
# y así sucesivamente.

class Persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def __eq__(self,objeto2):
        if self.edad==objeto2.edad:
            return True
        else:
            return False
    def __ne__(self,objeto2):
        if self.edad!=objeto2.edad:
            return True
        else:
            return False
    def __gt__(self,objeto2):
        if self.edad>objeto2.edad:
            return True
        else:
            return False
    def __ge__(self,objeto2):
        if self.edad>=objeto2.edad:
            return True
        else:
            return False
    def __lt__(self,objeto2):
        if self.edad<objeto2.edad:
            return True
        else:
            return False
    def __le__(self,objeto2):
        if self.edad<=objeto2.edad:
            return True
        else:
            return False

# bloque principal

# persona1=Persona('juan',22)
# persona2=Persona('ana',23)
# if persona1==persona2:
#     print("Las dos personas tienen la misma edad.")
# else:
#     print("No tienen la misma edad.")

#*****************************************************************
#2)
#Plantear una clase Rectangulo.
# Definir dos atributos (ladomenor y ladomayor).
# Redefinir el operador == de tal forma que tengan en cuenta la superficie del rectángulo.
# Lo mismo hacer con todos los otros operadores relacionales.

class Rectangulo:
    def __init__(self,lmenor,lmayor):
        self.lmenor=lmenor
        self.lmayor=lmayor
    def retornar_superficie(self):
        return self.lmenor*self.lmayor
    def __eq__(self,objeto2):
        if self.retornar_superficie()==objeto2.retornar_superficie():
            return True
        else:
            return False
    def __ne__(self,objeto2):
        if self.retornar_superficie()!=objeto2.retornar_superficie():
            return True
        else:
            return False
    def __gt__(self,objeto2):
        if self.retornar_superficie()>objeto2.retornar_superficie():
            return True
        else:
            return False
    def __ge__(self,objeto2):
        if self.retornar_superficie()>=objeto2.retornar_superficie():
            return True
        else:
            return False
    def __lt__(self,objeto2):
        if self.retornar_superficie()<objeto2.retornar_superficie():
            return True
        else:
            return False
    def __le__(self,objeto2):
        if self.retornar_superficie()<=objeto2.retornar_superficie():
            return True
        else:
            return False

# bloque principal

rectangulo1=Rectangulo(10,10)
rectangulo2=Rectangulo(5,20)
if rectangulo1==rectangulo2:
    print("Los rectangulos tienen la misma superficie")
else:
    print("Los rectangulos no tienen la misma superficie")

