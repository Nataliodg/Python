#El control visual Checkbutton permite implementar un botón de dos estados, más conocido como un cuadro de selección.
#1)
#Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación.
# Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados.

import tkinter as tk

class Aplication:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.selección1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text='Python', variable=self.selección1)
        self.check1.grid(column=0, row=0)
        self.selección2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1, text='C++', variable=self.selección2)
        self.check2.grid(column=0, row=1)
        self.selección3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1, text='JavaScript', variable=self.selección3)
        self.check3.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text='Verificar', command=self.verificar)
        self.boton1.grid(column=0, row=4)
        self.label1=tk.Label(self.ventana1, text='Cantidad: ')
        self.label1.grid(column=0, row=5)
        self.ventana1.mainloop()
    def verificar(self):
        cant=0
        if self.selección1.get()==1:
            cant+=1
        if self.selección2.get()==1:
            cant+=1
        if self.selección3.get()==1:
            cant+=1
        self.label1.configure(text='Cantidad:'+str(cant))

# aplicacion=Aplication()

#***********************************************************************************************
#2)
#Disponer un control Checkbutton que muestre el siguiente mensaje:
# ¿Está de acuerdo con los términos y condiciones?, además agregar un Button desactivo.
# Cuando se tilde el Checkbutton inmediatamente activar el botón.

class Aplicacion2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="¿Está de acuerdo con los términos y condiciones?", variable=self.seleccion, command=self.cambiarestado)
        self.check1.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana1, text="Entrar", state="disabled", command=self.ingresar)
        self.boton1.grid(column=0, row=1)        
        self.ventana1.mainloop()

    def cambiarestado(self):
        if self.seleccion.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion.get()==0:
            self.boton1.configure(state="disabled")

    def ingresar(self):
        self.ventana1.title("Ingresando...")

# aplicacion1=Aplicacion2()

#***********************************************************************************************
#2)
#Disponer varios objetos de la clase Checkbutton con nombres de navegadores web.
# En el título de la ventana mostrar todos los nombres de navegadores seleccionados.

class Aplicacion3:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Chrome", variable=self.seleccion1, command=self.cambiartitulo)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="FireFox", variable=self.seleccion2, command=self.cambiartitulo)
        self.check2.grid(column=1, row=0)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="Edge", variable=self.seleccion3, command=self.cambiartitulo)
        self.check3.grid(column=2, row=0)
        self.seleccion4=tk.IntVar()
        self.check4=tk.Checkbutton(self.ventana1,text="Opera", variable=self.seleccion4, command=self.cambiartitulo)
        self.check4.grid(column=3, row=0)
        self.ventana1.mainloop()

    def cambiartitulo(self):
        cadena='';
        if self.seleccion1.get()==1:
            cadena+="Chrome - "
        if self.seleccion2.get()==1:
            cadena+="Firefox - "
        if self.seleccion3.get()==1:
            cadena+="Edge - "
        if self.seleccion4.get()==1:
            cadena+="Opera"
        self.ventana1.title(cadena)

aplicacion1=Aplicacion3()