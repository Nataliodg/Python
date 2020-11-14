#Las aplicaciones de escritorio es muy común la necesidad de abrir otras ventanas emergentes con el objetivo de informar, advertir de errores etc.
# La librería tkinter provee un paquete llamado messagebox con una serie de funciones para la apertura de diálogos de información.
# Para usar estos diálogos lo primero que debemos hacer es importar el paquete:
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

#Podemos crear un alias para el nombre del paquete para no tener que escribir messagebox todas las veces.

#1)
#Confeccionar una aplicación que permita ingresar dos valores enteros y al presionar un botón nos muestre la suma en el título de la ventana.
# Si el operador no ingresa en alguno de los dos controles Entry datos informar mediante un diálogo el error que se está cometiendo.
# Agregar además un menú de opciones que al ser seleccionado nos muestre información del programa.

class Aplication:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.Labelframe(self.ventana1, text='Suma de números')
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.agregar_componentes()
        self.agregar_menu()
        self.ventana1.mainloop()
    
    def agregar_componentes(self):
        self.label1=ttk.Label(self.labelframe1, text='Ingrese primer valor: ')
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky='e')
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5,)
        self.label2=ttk.Label(self.labelframe1, text='Ingrese segundo valor: ')
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky='e')
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        self.boton1=ttk.Button(self.labelframe1, text='Sumar',command=self.sumar )
        self.boton1.grid(column=1, row=2, padx=5, pady=5, sticky='we')
    def agregar_menu(self):
        self.menubar1= tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1= tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label='Acerca de...', command=self.acerca)
        self.menubar1.add_cascade(label='Opciones', menu=self.opciones1)
    def sumar(self):
        if self.dato1.get()=="" or self.dato2.get()=="":
            mb.showerror('Cuidado','No puede dejar los cuadros de entrada de números vacíos')
        else:
            suma=int(self.dato1.get())+int(self.dato2.get())
            self.ventana1.title('La suma es '+str(suma))
    def acerca(sef):
        mb.showinfo('Información', 'Este programa fue desarrollado para el apredizaje de Python y tkinter')

aplicacion1=Aplication()