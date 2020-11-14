#Una de las herramientas fundamentales cuando armamos interfaces visuales es la metodología
# que utilizamos para disponer los controles dentro del formulario.
# Hasta ahora hemos utilizado el administrador de diseño Grid.
#En la librería GUI tkinter disponemos de tres Layout Manager para disponer controles dentro de una ventana:
# Grid
# Pack
# Place
#Solo se puede utilizar uno de estos Layout Manager dentro de un contenedor,
# recordemos que un contenedor puede ser la ventana propiamente dicha,
# un Frame o un LabelFrame.
#El gestor de diseño más completo y que se adapta en la mayoría de las situaciones es el Grid,
# pero podemos en muchos casos crear Frame o LabelFrame y definir dentro de estos Layout Manager de tipo Pack o Place.

#Layout Manager: Pack
# Veamos con un ejemplo como se ubican los Widget utilizando Pack.

#1)
# Disponer una serie de botones utilizando el Layout Manager de tipo Pack.

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text='Boton 1')
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH)#Si se quiere agregar espacios entre cada boton(padx=25, pady=25)
        self.boton2=ttk.Button(self.ventana1, text='Boton 2')
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana1, text='Boton 3')
        self.boton3.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton4=ttk.Button(self.ventana1, text='Boton 4')
        self.boton4.pack(side=tk.LEFT)
        self.boton5=ttk.Button(self.ventana1, text='Boton 5')
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana1, text='Boton 6')
        self.boton6.pack(side=tk.RIGHT)
        self.boton7=ttk.Button(self.ventana1, text='Boton 7')
        self.boton7.pack(side=tk.RIGHT)
        self.ventana1.mainloop()

# aplicacion1=Aplicacion()

#****************************************************************
#2)
#Layout Manager: Grid
#Este tipo de Layout Manager lo hemos estado utilizando en muchos conceptos anteriores, veremos otras posibilidades que nos suministra.
# Este tipo de Layout define una tabla con columnas y filas, cada vez que agregamos un Widget indicamos en que columna y fila se debe ubicar

#Disponer una serie de botones utilizando el Layout Manager de tipo Grid.

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1, text="Boton 1")
        self.boton1.grid(column=0, row=0)
        self.boton2=ttk.Button(self.ventana1, text="Boton 2")
        self.boton2.grid(column=1, row=0)
        self.boton3=ttk.Button(self.ventana1, text="Boton 3")
        self.boton3.grid(column=2, row=0, rowspan=2, sticky="ns")#En la propiedad sticky, pedimos que el botón se expanda de north (norte) a south (sur), si no disponemos sticky luego el botón ocupa las dos celdas pero aparece centrado.
        self.boton4=ttk.Button(self.ventana1, text="Boton 4")
        self.boton4.grid(column=0, row=1)
        self.boton5=ttk.Button(self.ventana1, text="Boton 5")
        self.boton5.grid(column=1, row=1)
        self.boton6=ttk.Button(self.ventana1, text="Boton 6")
        self.boton6.grid(column=0, row=2, columnspan=3, sticky="we")#En el parámetro sticky indicamos que se estire de west (oeste) a east (este)
        self.ventana1.mainloop()

# aplicacion1=Aplicacion2()

#****************************************************************
#3)
#Una de las herramientas fundamentales cuando armamos interfaces visuales es la metodología

#Layout Manager: Place
#Este tipo de Layout Manager nos permite disponer un Widget en una posición y con un tamaño con valor absoluto a nivel de píxeles.
# Hay que tener cuidado en que casos utilizar este tipo de administrador de diseños ya que si agrandamos o reducimos el tamaño de la ventana
# puede ser que los controles queden fuera de la ventana y el operador no pueda visualizarlos.
#Problema:
#Disponer dos botones en la parte inferior derecha de la ventana utilizando el Layout Manager de tipo Place.
# El ancho y alto de la ventana debe ser de 800 por 600 píxeles.

class Aplicacion3:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry('800x600')
        self.ventana1.resizable(0,0)#No permitimos que el operador la redimensione con el mouse (esto debido a que si reduce el tamaño los botones quedarán fuera de la ventana)
        self.boton1=ttk.Button(self.ventana1, text='Confirmar')
        self.boton1.place(x=680, y=550, width=90, height=30)
        self.boton1=ttk.Button(self.ventana1, text='Cancelar')
        self.boton1.place(x=580, y=550, width=90, height=30)
        self.ventana1.mainloop()

aplicacion=Aplicacion3()