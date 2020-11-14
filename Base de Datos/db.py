import mysql.connector

midb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Python13mysql9',
    database='prueba'
)

cursor= midb.cursor()
#Listar Datos:

# cursor.execute('select * from Usuario')
# resultado= cursor.fetchall()#Muestra todos los ficheros
# print(resultado)

#Limitar cantidad de elementos:

cursor.execute('select * from Usuario limit 1')
resultado= cursor.fetchall()#Muestra todos los ficheros
print(resultado)

#resultado= cursor.fetchone()#Muestra el primer fichero


#Ver definiciones de tablas:

#cursor.execute('show create table Usuario')#Muestra el contenido y módelo de la tabla

#Insertar Datos:
# sql= 'insert into Usuario (Email, Username, Edad) values (%s, %s, %s)'#Ingresar
# values=('nata@correo.com', 'Natalio', 25)

#Actualizar Datos:

# sql= 'update Usuario set Email = %s where Id = %s'
# values= ('micorreo@correo.com', 4)

# #Consultar:
# cursor.execute(sql,values)

# midb.commit()
# print(cursor.rowcount)

#Eliminar Datos:

# sql= 'delete from Usuario where Id= %s'
# values= (4, )
# cursor.execute(sql, values)
# midb.commit()



