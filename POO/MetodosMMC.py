#1)
#Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación y división.
# Hacer cada operación en otro método de la clase Operación y llamarlos desde el mismo método __init__

class Operation:
    def __init__(self):
        self.valor1=int(input('Ingrese primer valor:'))
        self.valor2=int(input('Ingrese segundo valor:'))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
    def sumar(self):
        suma=self.valor1+self.valor2
        print('La suma es:',suma)
    def restar(self):
        resta=self.valor1-self.valor2
        print ('La resta es:',resta)
    def multiplicar(self):
        multi=self.valor1*self.valor2
        print('El prodcuto es:',multi)
    def dividir(self):
        division=self.valor1/self.valor2
        print('La división es:',division)

#Bloque Principal

# operacion=Operation()

#*****************************************************************
#2)
#Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas.
# Mostrar un menú de opciones que permita:
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa.

class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()

    def cargar(self):
        for x in range(5):
            nom=input("Ingrese nombre del alumno:")
            self.nombres.append(nom)
            no=int(input("Nota del alumno:"))
            self.notas.append(no)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print(self.nombres[x],self.notas[x])
        print("_____________________")            

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print(self.nombres[x],self.notas[x])
        print("_____________________")                


# bloque principal

# alumnos=Alumnos()
# alumnos.menu()

#****************************************************************
#3)
#Confeccionar una clase que administre una agenda personal.
# Se debe almacenar el nombre de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa.

class Agenda:

    def __init__(self):
        self.contactos={} # definimos un diccionario para almacenar los datos

    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de la agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Modificacion del telefono y mail")
            print("5- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listado()
            elif opcion==3:
                self.consulta()
            elif opcion==4:
                self.modificacion()

    def cargar(self):
        nombre=input("Ingrese el nombre de la persona:")
        telefono=input("Ingrese el numero de telefono:")
        mail=input("Ingrese el mail:")
        self.contactos[nombre]=(telefono,mail)
        print("______________________________________________")
        
    def listado(self):
        print("______________________________________________")        
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print('Nombre:',nombre,'Contacto:', self.contactos[nombre][0],'Mail:',self.contactos[nombre][1])
        print("______________________________________________")

    def consulta(self):
        print("______________________________________________")        
        nombre=input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:
            print(nombre," su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")            

    def modificacion(self):
        print("______________________________________________")        
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo mail:")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contaxto con ese nombre")
        print("______________________________________________")         
        

# bloque principal

agenda=Agenda()
agenda.menu()

