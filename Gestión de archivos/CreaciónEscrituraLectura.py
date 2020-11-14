#Un archivo de texto contiene un conjunto de caracteres estructurados en distintas líneas.
# Es un formato de archivo ampliamente utilizado como pueden ser:
# El código fuente de un script en Python se almacena en un archivo de texto (igual que cualquier otro lenguaje de programación)
# Archivos HTML, CSS, XML se almacenan en archivos de texto.
# Archivos JSON etc.

#Creación de un archivo de texto y almacenamiento de datos.
#Como es una actividad tan común en todo programa el lenguaje Python 
# incluye por defecto todas las funcionalidades para trabajar con archivos de texto.
#Veamos con un ejemplo como crear y almacenar caracteres en un archivo de texto.

#1)
#Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto.
# Abrir luego el archivo creado con un editor de texto.

# archivo1=open('datos.txt','w')
# archivo1.write('Primera línea.\n')
# archivo1.write('Segunda línea.\n')
# archivo1.write('Tercera línea.\n')
# archivo1.close()

#*****************************************************************
#2)
#Leer el contenido del archivo de texto 'datos.txt'.

# archivo1=open('datos.txt', 'r')
# contenido=archivo1.read()
# print(contenido)
# archivo1.close

#*****************************************************************
#Lectura de un archivo de texto línea a línea.
#En algunas situaciones podemos necesitar leer el contenido de un archivo de texto línea a línea.
# Disponemos de un método llamado 'readline' que lee una línea completa del archivo, inclusive retorna el caracter '\n' de fin de línea.
#3)
#Leer el contenido del archivo de texto 'datos.txt' línea a línea.

# archivo1=open('datos.txt', 'r')
# linea=archivo1.readline()

# while linea!= '':
#     print(linea, end='')
#     linea= archivo1.readline()
# archivo1.close()

#Con estructura For:

# archivo1=open('datos.txt', 'r')
# for linea in archivo1:
#     print(linea, end='')
# archivo1.close()

#*****************************************************************
#4)
#Almacenar un archivo de texto en una lista
# #Mediante el método 'readlines' podemos recuperar cada una de las líneas del archivo de texto y almacenarlas en una lista.

#Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista.
# Imprimir la cantidad de líneas que tiene el archivo y su contenido.

# archivo1=open('datos.txt', 'r')
# lineas=archivo1.readlines()
# print('El archivo tiene', len(lineas), 'lineas')
# print('El contenido del archivo')
# for linea in lineas:
#     print(linea, end='')
# archivo1.close()

#*****************************************************************
#5)
#Abrir un archivo de texto para añadir líneas.
# Hemos visto que cuando llamamos a la función 'open' el segundo parámetro puede ser "w", "r" y
# si queremos que se abra para añadir sin borrar las líneas actuales del archivo debemos hacerlo con el parámetro "a" (append).

#Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas.
# Imprimir luego el archivo completo.

# archivo1=open('datos.txt', 'a')
# archivo1.write('Nueva linea 1 \n')
# archivo1.write('nueva linea 2 \n')
# archivo1.close()

# archivo1=open('datos.txt', 'r')
# contenido=archivo1.read()
# print(contenido)
# archivo1.close()

#*****************************************************************
#5)
#Abrir un archivo para leer y agregar datos.
# Hay una cuarta forma de abrir un archivo indicando en el segundo parámetro de la función open el string "r+", con dicha opción podemos leer y escribir.

#Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y agregar luego dos líneas al final.

# archivo1=open('datos.txt', 'r+')
# contenido=archivo1.read()
# print(contenido)

# archivo1.write('Otra linea 1\n')
# archivo1.write('Otra linea 2\n')
# archivo1.close()

#******************************************************************
#6)
#Codificación de caracteres utf-8.
#Actualmente se utiliza mucho la codificación de caracteres utf-8
# la que nos permite representar una infinidad de caracteres de distintos idiomas y símbolos.
#En Python debemos indicar cuando abrimos el archivo de texto mediante el parámetro 'encoding' la codificación de caracteres utilizada.

#Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto.
# Abrir luego el archivo creado con el editor VS Code.

archivo1=open('datos.txt', 'w', encoding='utf-8')
archivo1.write('Primer linea.\n')
archivo1.write('Segunda linea.\n')
archivo1.write('Tercer linea.\n')
archivo1.close()


