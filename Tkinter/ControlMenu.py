#Para implementar los típicos menú de barra horizontales que aparecen en las aplicaciones cuando utilizamos la librería Tk
# necesitamos crear objetos de la clase Menu que se encuentra declarada en el paquete tkinter y no en el paquete tkinter.ttk.
#Veremos con un ejemplo implementar un menú con una serie de opciones.

#1)
#Confeccionar una aplicación que muestre dos opciones en el menú de barra superior.
# La primer opción despliega un submenú que permita cambiar el color de fondo del formulario y
# la segunda permita cambiar el tamaño de formulario:

import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo", command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

# aplicacion1=Aplicacion()

#*****************************************************************
#2)
#Otra posibilidad es agregar teclas de acceso rápido a opciones de nuestro menú. Esto se resuelve la parte visual agregando el parámetro 'acelerator',
# y por otro lado asignar a cada una de las teclas de acceso rápido la ejecución de un método:

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Rojo", command=self.fijarrojo, accelerator="Ctrl+R")
        opciones1.add_command(label="Verde", command=self.fijarverde, accelerator="Ctrl+V")
        opciones1.add_separator()        
        opciones1.add_command(label="Azul", command=self.fijarazul, accelerator="Ctrl+A")
        self.ventana1.bind_all("<Control-r>", self.cambiar)
        self.ventana1.bind_all("<Control-v>", self.cambiar)
        self.ventana1.bind_all("<Control-a>", self.cambiar)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

    def cambiar(self, event):
        if event.keysym=="r":
            self.fijarrojo()
        if event.keysym=="v":
            self.fijarverde()
        if event.keysym=="a":
            self.fijarazul()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

# aplicacion1=Aplicacion2()

#********************************************************************
#3)
#Podemos disponer dentro de un menú desplegable una opción que despliegue otro submenú, la interfaz visual debe ser similar a esta:

class Aplicacion3:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo", command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores", menu=opciones1)        
        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        submenu1=tk.Menu(menubar1)
        submenu1.add_command(label="1024x1024", command=self.tamano1)
        submenu1.add_command(label="1280x1024", command=self.tamano2)        
        opciones2.add_cascade(label="Otros tamaños", menu= submenu1)        
        menubar1.add_cascade(label="Tamaños", menu=opciones2)        
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

    def tamano1(self):
        self.ventana1.geometry("1024x1024")

    def tamano2(self):
        self.ventana1.geometry("1280x1024")

# aplicacion1=Aplicacion3()

#*****************************************************************
#4)
#Mediante dos controles de tipo Entry permitir el ingreso de dos números.
# Crear un menú que contenga una opción que cambie el tamaño de la ventana con los valores ingresados por teclado.
# Finalmente disponer otra opción que finalice el programa

class Aplicacion4:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Cambiar dimensión ventana", command=self.fijartamano)
        opciones1.add_command(label="Finalizar", command=self.finalizar)
        menubar1.add_cascade(label="Opciones", menu=opciones1)
        self.label1=ttk.Label(text="Ingrese ancho de la ventana en X:")
        self.label1.grid(column=0, row=0)
        self.ancho=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=10, textvariable=self.ancho)
        self.entry1.grid(column=0, row=1)        
        self.label2=ttk.Label(text="Ingrese ancho de la ventana en Y:")
        self.label2.grid(column=0, row=2)
        self.alto=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=10, textvariable=self.alto)
        self.entry2.grid(column=0, row=3)        

        self.ventana1.mainloop()

    def fijartamano(self):
        self.ventana1.geometry(self.ancho.get()+"x"+self.alto.get())

    def finalizar(self):
        sys.exit()

aplicacion1=Aplicacion4()