#1)
#Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer",
# cuando se presione un botón actualizar una Label con el Radiobutton seleccionado.

import tkinter as tk

class Aplication:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1, text='Varon', variable=self.seleccion, value=1 )
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text='Mujer', variable=self.seleccion, value=2 )
        self.radio2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text='Mostrar seleccionado', command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(self.ventana1, text='Opcion Seleccionada')
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()
    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            self.label1.configure(text='Opcion Seleccionado: Varon')
        if self.seleccion.get()==2:
            self.label1.configure(text='Opcion Seleccionado: Mujer')

# aplicacion=Aplication()

#****************************************************************
#2)
#Disponer dos controles de tipo Entry para el ingreso de enteros.
# Mediante dos controles Radiobutton permitir seleccionar si queremos sumarlos o restarlos.
# Al presionar un botón mostrar el resultado de la operación seleccionada.

class Aplication2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text='Ingrese primer valor: ')
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1 )
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(self.ventana1, text='Ingrese segundo valor: ')
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.seleccion=tk.IntVar()
        self.radio1=tk.Radiobutton(self.ventana1, text='Sumar', variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=2)
        self.radio2=tk.Radiobutton(self.ventana1, text='Restar', variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1, text='Operar', command=self.operar)
        self.boton1.grid(column=1, row=4)
        self.label3=tk.Label(self.ventana1, text='Resultado')
        self.label3.grid(column=1, row=5)
        self.ventana1.mainloop()
    def operar(self):
        if self.seleccion.get()==1:
            suma=int(self.dato1.get()) + int(self.dato2.get())
            self.label3.configure(text=suma)
        if self.seleccion.get()==2:
            resta= int(self.dato1.get()) - int(self.dato2.get())
            self.label3.configure(text=resta)

# aplicacion=Aplication2()

#****************************************************************
#3)
#Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'.
# Cuando se presione un botón cambiar el color de fondo del formulario.
# Si consideramos que la variable ventana1 es un objeto de la clase Tk,
# luego si queremos que el fondo sea de color rojo debemos llamar al método configure y
# en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue")

class Aplication3:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.radio1=tk.Radiobutton(self.ventana1, text='Rojo', variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text='Verde', variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.radio3=tk.Radiobutton(self.ventana1, text='Azul', variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text='Cambiar color', command=self.activar)
        self.boton1.grid(column=0, row=3)
        self.ventana1.mainloop()
    def activar(self):
        if self.seleccion.get()==1:
            self.ventana1.configure(bg='red')
        if self.seleccion.get()==2:
            self.ventana1.configure(bg='green')
        if self.seleccion.get()==3:
            self.ventana1.configure(bg='blue')

aplicacion=Aplication3()
