#1)
#Definir una clase Cliente que almacene un código de cliente y un nombre.
# En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas corrientes.
# Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.

class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


# bloque principal

# cliente1=Cliente(1,"Juan")
# cliente2=Cliente(2,"Ana")
# cliente3=Cliente(3,"Diego")
# cliente4=Cliente(4,"Pedro")

# cliente3.suspender()
# cliente4.suspender()

# cliente1.imprimir()   
# cliente2.imprimir()
# cliente3.imprimir()
# cliente4.imprimir()

# print(Cliente.suspendidos)

#*****************************************************************
#2)
#Plantear una clase llamada Jugador.
# Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
# Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
# Definir en el bloque principal dos objetos de la clase Jugador.
# Reducir dicha variable hasta llegar a cero.

class Jugador:
    tiempo=30

    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Puntaje:",self.puntaje)
        print("Fin de juego en",Jugador.tiempo,"minutos")

    def pasar_minuto(self):
        Jugador.tiempo=Jugador.tiempo-1


# bloque principal

jugador1=Jugador("Juan",100)
jugador2=Jugador("Ana",50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minuto()


