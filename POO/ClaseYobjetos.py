#La programación orientada a objetos se basa en la definición de clases; a diferencia de la programación estructurada, que está centrada en las funciones.
# Una clase es un molde del que luego se pueden crear múltiples objetos, con similares características.
# Un poco más abajo se define una clase Persona y luego se crean dos objetos de dicha clase.
# Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos (lo que conocemos como funciones).
# La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá sus propios valores y compartirán las mismas funciones.
#Debemos declarar una clase antes de poder crear objetos (instancias) de esa clase.
# Al crear un objeto de una clase, se dice que se crea una instancia de la clase o un objeto propiamente dicho.

#*****************************************************************
#1)
#Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), 
# uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
# Definir dos objetos de la clase Persona.

class Person:
    def initialize(self,nom):#inicializar
        self.name=nom
    def print2(self):
        print('Name:',self.name)

#Bloque Principal
# person1=Person()
# person1.initialize('Natalio')
# person1.print2()

# person2=Person()
# person2.initialize('Nati')
# person2.print2()

#*****************************************************************
#2)
#Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
#Definir dos objetos de la clase Alumno.

class Student:
    def initialize2(self,name,note):
        self.name=name
        self.note=note
    def print3(self):
        print('Name:',self.name)
        print('Note:',self.note)
    def  showStatus(self):
        if self.note>=4:
            print('Regular.')
        else:
            print('Vacant.')

#Bloque Principal

# student1=Student()
# student1.initialize2('Nata',7)
# student1.print3()
# student1.showStatus()

# student2=Student()
# student2.initialize2('Ana',2)
# student2.print3()
# student2.showStatus()

#*****************************************************************
#3)
#Confeccionar una clase que permita carga el nombre y la edad de una persona.
# Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Person:
    def initialize(self,name,age):
        self.name=name
        self.age=age
    def printP(self):
        print('Name:',self.name,'Age:',self.age)
    def majorAge(self):
        if self.age>=18:
            print('Is older')#Es Mayor.
        else:
            print('Is a minor')#Es Menor.


#Bloque Principal

# person1=Person()
# person1.initialize('Nata',25)
# person1.printP()
# person1.majorAge()

# person2=Person()
# person2.initialize('Mica',9)
# person2.printP()
# person2.majorAge()

#*****************************************************************
#4)
#Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
# inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
#El nombre de la clase llamarla Triangulo.

class Triangle:
    def initialize(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def printMajor(self):
        if self.lado1>=self.lado2 and self.lado1>=self.lado3:
            print('El lado mayor es:',self.lado1)
        else:
            if self.lado2>=self.lado3:
                print('El lado mayor es:',self.lado2)
            else:
                print('El lado mayor es:',self.lado3)
    def printEquilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print('Es un triangulo equilatero.')
        else:
            print('No es equilatero')
    def printL(self):
        print('Valores de los lados del Triangulo.')
        print('Lado 1:',self.lado1)
        print('Lado 2:',self.lado2)
        print('Lado 3:',self.lado3)

#Bloque Principal:
triangle=Triangle()
triangle.initialize(10,10,100)
triangle.printMajor()
triangle.printEquilatero()
triangle.printL()