#El control visual LabelFrame tiene una funcionalidad casi idéntica a la componente Frame que vimos en el concepto anterior,
# la única diferencia es que agrega un texto en la parte superior del Frame y hace un recuadro alrededor del mismo.
#El Widget LabelFrame es un contenedor donde podemos agregar en su interior otros Widget como Button, Label, Entry, Radiobutton etc.

#1)
#Confeccionar una aplicación que muestre dos controles de tipo LabelFrame.
# En la primera disponer 2 Label, 2 Entry y un Button, en el segundo LabelFrame disponer 3 botones.

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.Labelframe(self.ventana1, text='Login:')
        self.labelframe1.grid(column=0, row=1, padx=5, pady=10)
        self.login()
        self.labelframe2=ttk.Labelframe(self.ventana1, text='Operaciones')
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.operaciones()
        self.ventana1.mainloop()
    
    def login(self):
        self.label1=ttk.Label(self.labelframe1, text='Nombre de usuario:' )
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text='Ingrese clave:' )
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1)
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text='Ingresar')
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
    
    def operaciones(self):
        self.boton2=ttk.Button(self.labelframe2, text='Agregar usuario')
        self.boton2.grid(column=0, row=0, padx=4, pady=4)
        self.boton3=ttk.Button(self.labelframe2, text='Modificar usuario')
        self.boton3.grid(column=1, row=0, padx=4, pady=4)
        self.boton4=ttk.Button(self.labelframe2, text='Borrar usuario')
        self.boton4.grid(column=2, row=0, padx=4, pady=4)

# aplicacion1=Aplicacion()

#****************************************************************
#2)

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.Labelframe(self.ventana1, text='Artículo')
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.articulo()
        self.labelfram2=ttk.Labelframe(self.ventana1, text='Operaciones')
        self.labelfram2.grid(column=0, row=1, padx=5, pady=10)
        self.operaciones()
        self.ventana1.mainloop()
    
    def articulo(self):
        self.label1=ttk.Label(self.labelframe1, text='Código de artículo:')
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1, show='*')
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text='Descripción:')
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1, show='*')
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text='Precio:')
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.entry3=ttk.Entry(self.labelframe1, show='*')
        self.entry3.grid(column=1, row=2, padx=4, pady=4)
    
    def operaciones(self):
        self.boton1=ttk.Button(self.labelfram2, text='Alta')
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelfram2, text='Baja')
        self.boton2.grid(column=1, row=0, padx=4, pady=4)
        self.boton3=ttk.Button(self.labelfram2, text='Modificacion')
        self.boton3.grid(column=20, row=0, padx=4, pady=4)

aplicacion2=Aplicacion2()
