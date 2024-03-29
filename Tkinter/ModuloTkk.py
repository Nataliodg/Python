#Tk hemos dicho que es una biblioteca de controles visuales que los podemos acceder desde Python y desde otros lenguajes de programación.
#En la versión Tk 8.5 sumó una nueva serie de controles visuales ( Notebook, Combobox etc.) y modernizó los que hemos visto en los conceptos anteriores.
# Para hacer uso de esta nueva versión de la biblioteca en Python se implementó un nuevo módulo y se lo agregó al paquete tkinter.
# Para hacer uso de este conjunto de Widget (controles visuales) debemos importar el paquete ttk.
# Todo lo que conocemos hasta ahora de los controles visuales del módulo tkinter funciona prácticamente sin cambios, lo que deberemos hacer es crear objetos de la clase Button, Entry etc. recuperándolos ahora del módulo tkinter.ttk

#1)
#Mostrar una ventana y en su interior dos botones y una label utilizando el módulo ttk. La label muestra inicialmente el valor 1.
# Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.label1=ttk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=ttk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=ttk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


# aplicacion1=Aplicacion()

#*****************************************************************
#2)
#Ingresar el nombre de usuario y clave en controles de tipo Entry.
# Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
# Utilizar Widget del módulo ttk.

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=ttk.Label(text="Ingrese clave:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=ttk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

# aplicacion1=Aplicacion2() 

#***************************************************************
#3)
#Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer",
# cuando se presione un botón actualizar una Label con el Radiobutton seleccionado.

class Aplicacion3:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=ttk.Radiobutton(self.ventana1,text="Varon", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=ttk.Radiobutton(self.ventana1,text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.boton1=ttk.Button(self.ventana1, text="Mostrar seleccionado", command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)
        self.label1=ttk.Label(text="opcion seleccionada")
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="opcion seleccionada=Varon")
        if self.seleccion.get()==2:
            self.label1.configure(text="opcion seleccionada=Mujer")

# aplicacion1=Aplicacion3()

#****************************************************************
#4)
#Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación.
# Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados.
# Utilizar Widget del módulo ttk.

class Aplicacion4:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=ttk.Checkbutton(self.ventana1,text="Python", variable=self.seleccion1)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=ttk.Checkbutton(self.ventana1,text="C++", variable=self.seleccion2)
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=ttk.Checkbutton(self.ventana1,text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)
        self.boton1=ttk.Button(self.ventana1, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=4)
        self.label1=ttk.Label(text="cantidad:")
        self.label1.grid(column=0, row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=0
        if self.seleccion1.get()==1:
            cant+=1
        if self.seleccion2.get()==1:
            cant+=1
        if self.seleccion3.get()==1:
            cant+=1
        self.label1.configure(text="cantidad:"+str(cant))


# aplicacion1=Aplicacion4()

#*****************************************************************
#5)
#Disponer un Listbox con una serie de nombres de frutas.
# Permitir la selección solo de uno de ellos.
# Cuando se presione un botón recuperar la fruta seleccionada y mostrarla en una Label.

class Aplicacion5:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=ttk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=ttk.Label(text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion5()
