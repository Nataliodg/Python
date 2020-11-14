#En las interfaces visuales las ventanas son controles visuales contenedores de otros controles como los botones y etiquetas de texto.
# Veremos los pasos que debemos dar si queremos que se muestren objetos de la clase Button y Label en nuestras ventanas.

#1)
#Mostrar una ventana y en su interior dos botones y una label.
# La label muestra inicialmente el valor 1.
# Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label

import tkinter as tk
import sys
class Aplication:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title('Controles Button y Label')
        self.labell=tk.Label(self.ventana1, text=self.valor)
        self.labell.grid(column=0,row=0)
        self.labell.configure(foreground='red')
        
        self.boton1=tk.Button(self.ventana1, text='Incrementar', command=self.incrementar)
        self.boton1.grid(column=0, row=1)
        
        self.boton2=tk.Button(self.ventana1, text='Decrementar', command=self.decrementar)
        self.boton2.grid(column=0, row=2)
        
        self.ventana1.mainloop()
    def incrementar(self):
        self.valor=self.valor+1
        self.labell.config(text=self.valor)
    def decrementar(self):
        self.valor=self.valor-1
        self.labell.config(text=self.valor)

# aplicacion1=Aplication()

#*****************************************************************
#2)
#Mostrar dos Label, en una se muestra el nombre del programa y en la segunda el año de creación.
# Disponer un botón para finalizar el programa.
# No permitir al usuario redimensionar la ventana.

class Aplication2:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title('Prueba')
        self.label1=tk.Label(self.ventana1, text='Sistema de faturación')
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text='2020')
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text='Finalizar', command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False,False)
        self.ventana1.mainloop()
        
    def finalizar(self):
        sys.exit(0)

# aplicacion2=Aplication2()

#*****************************************************************
#3)
#Disponer dos objetos de la clase Button con las etiquetas:
# "varón" y "mujer", al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.

class Aplication3:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title('Prueba')
        self.boton1=tk.Button(self.ventana1, text='Varón', command=self.presionovaron)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text='Mujer', command=self.presionomujer)
        self.boton2.grid(column=0, row=1)
        self.ventana1.mainloop()
    def presionovaron(self):
        self.ventana1.title('Varón')
    def presionomujer(self):
        self.ventana1.title('Mujer')

# aplicacion3=Aplication3()

#*****************************************************************
#4)
#Mostrar los botones del 1 al 5.
# Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento.

class Aplication4:
    def __init__(self):
        self.datos=''
        self.ventana1=tk.Tk()
        self.ventana1.title('Prueba')
        self.boton1=tk.Button(self.ventana1, text='1', command=self.presion1)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text='2', command=self.presion2)
        self.boton2.grid(column=1, row=0)
        self.boton3=tk.Button(self.ventana1, text='3', command=self.presion3)
        self.boton3.grid(column=2, row=0)
        self.boton4=tk.Button(self.ventana1, text='4', command=self.presion4)
        self.boton4.grid(column=3, row=0)
        self.boton5=tk.Button(self.ventana1, text='5', command=self.presion5)
        self.boton5.grid(column=4, row=0)
        self.label1=tk.Label(self.ventana1, text=self.datos)
        self.label1.grid(column=5, row=0)
        self.ventana1.mainloop()
        
    def presion1(self):
        self.datos= self.datos+'1'
        self.label1.configure(text=self.datos)
    def presion2(self):
        self.datos= self.datos+'2'
        self.label1.configure(text=self.datos)
    def presion3(self):
        self.datos= self.datos+'3'
        self.label1.configure(text=self.datos)
    def presion4(self):
        self.datos= self.datos+'4'
        self.label1.configure(text=self.datos)
    def presion5(self):
        self.datos= self.datos+'5'
        self.label1.configure(text=self.datos)

aplicacion4=Aplication4()