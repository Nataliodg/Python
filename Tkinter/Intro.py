#1)
#Mostrar una ventana y que en su título aparezca el mensaje 'Hola Mundo'.
# El programa en Python haciendo uso del módulo 'tkinter' requiere el siguiente algoritmo:

# import tkinter as tk

# ventana1=tk.Tk()
# ventana1.title("Hola Mundo")
# ventana1.mainloop()

#Aplicación orientada a objetos.
# Todos los ejemplos que haremos de ahora en más independientemente de su complejidad utilizaremos la metodología de POO (Programación Orientada a Objetos)
#El programa anterior modificado con POO queda:

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.ventana1.mainloop()


aplicacion1=Aplicacion()

#Planteamos una clase llamada 'Aplicacion' y en su método '__init__' creamos el objeto de la clase 'Tk' para que se muestre la ventana.
# Debemos crear luego un objeto de la clase 'Aplicacion':
# aplicacion1=Aplicacion()


