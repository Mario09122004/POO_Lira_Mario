import mysql.connector
from mysql.connector import Error

    
connection = mysql.connector.connect(
        host='localhost',
        password='',
        user='root',
        database='controlescolar',
    )
cursor = connection.cursor()

if connection.is_connected():
    print("Conexión exitosa a la base de datos")
    
def insertar():
    query = "INSERT INTO profesores (nombre, correo, direccion) VALUES (%s, %s, %s)"
    cursor.execute(query, ("test", "Algun correo", "Vivira por algun lado"))
    connection.commit()
    print("Profesor insertado exitosamente")

def mostrar():
    cursor.execute("SELECT * FROM profesores")
    result = cursor.fetchall()
    for row in result:
        print(row)

def borrar():
    mostrar()
    id = input("ingresar el id a borrar:")
    query = "DELETE FROM profesores WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print("Profesor eliminado exitosamente")

def actualizar():
    mostrar()
    id = input("ingresar el id a modificar:")
    query = "UPDATE profesores SET nombre = %s, correo = %s, direccion = %s WHERE id = %s"
    cursor.execute(query, ("cambio", "cambio", "se mudo", id))
    connection.commit()
    print("Profesor actualizado exitosamente")

######################################

insertar()
insertar()
insertar()
mostrar()
borrar()
actualizar()

######################################

if connection.is_connected():
    connection.close()
    print("Conexión cerrada")