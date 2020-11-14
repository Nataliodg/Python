#El control Combobox del paquete ttk permite seleccionar un string de un conjunto de items que se despliegan.
# Podemos indicar cual elemento muestre por defecto mediante el método 'current'.
# Por defecto el operador puede además de seleccionar un elemento cargar por teclado cualquier cadena.

#1)
#Mostrar en una ventana un control de tipo Combobox con los días de la semana.
# Cuando se presione un botón actualizar una Label con el día seleccionado.

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Seleccione un día de la semana")
        self.label1.grid(column=0, row=0)
        self.opcion=tk.StringVar()
        diassemana=("lunes","martes","miércoles","jueves","viernes","sábado","domingo")
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=10, 
                                  textvariable=self.opcion, 
                                  values=diassemana)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)
        self.label2=ttk.Label(self.ventana1, text="Día seleccionado:")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text=self.opcion.get())

# aplicacion1=Aplicacion()

#******************************************************************
#2)
#Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país.
# Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(text="Ingrese nombre")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=40, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)
        self.label2=ttk.Label(text="Seleccione país")
        self.label2.grid(column=0, row=2)
        self.pais=tk.StringVar()
        paises=("Argentina","Chile","Bolivia","Paraguay","Brasil","Uruguay")
        self.combobox1=ttk.Combobox(self.ventana1, 
                                    width=10, 
                                    textvariable=self.pais, 
                                    values=paises,
                                    state='readonly')
        #self.combobox1.current(0)                                
        self.combobox1.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.mostrardatos)
        self.boton1.grid(column=0, row=4)        
        self.ventana1.mainloop()

    def mostrardatos(self):
        self.ventana1.title("Nombre:"+self.nombre.get()+" Pais:"+self.combobox1.get())

aplicacion1=Aplicacion2() 