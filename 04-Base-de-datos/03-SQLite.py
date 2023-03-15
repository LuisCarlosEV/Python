import sqlite3, json
#connection = sqlite3.connect("demo.db")
connection = sqlite3.connect("Luis Carlos/Python/04-Base-de-Datos/demo.db")
#connection = sqlite3.connect(":memory:")

#creamos el cursor que nos permite ejecutar comandos contra la base de datos

cursor = connection.cursor()

#Consultamos la existencia de una tabla en la base de datos
#Si la tabla no exite, se crea

command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'" #count() sirve para contabilizar #sqlite es una base de datos interna comun a todas
cursor.execute(command)
numTablas = cursor.fetchone()[0]
print(f"Numero de tablas Alumnos: {numTablas}")

if(numTablas == 0):
    command = "CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)
    print("Numero de tablas creadas", cursor.rowcount)


exit()
#Consultar datos con SELECT
command = "SELECT * FROM Alumnos"
cursor.execute(command)

row = cursor.fetchone()
while(row):
    print(row)
    row = cursor.fetchone()

print("")

cursor.execute(command)
for row in cursor.fetchall():
    print(row)

#Inserccion masiva
lista = [
    ('002', 'Ana', 'Trujillo', '2C', None),
    ('003', 'Adrian', 'Sanz', '2A', json.dumps([7.5, 6, 9, 5, 6.9])),
    ('004', 'Maria', 'Sanchez', '2b', None),
]
command = "INSERT INTO ALUMNOS VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, lista)
connection.commit()
print("Numero de registros insertados: ", cursor.rowcount)


#Insertamos con INSERT
command = "INSERT INTO Alumnos (id, nombre) VALUES ('000', 'Borja')"
cursor.execute(command)
connection.commit()
print("Numero de registros insertados: ", cursor.rowcount)

#Actualizar un registro utilizando UPDATE
command = "UPDATE Alumnos SET Apellidos = 'Cabeza' WHERE id = '000'"
cursor.execute(command)
connection.commit()
print("Numero de registros modificados: ", cursor.rowcount)

#Modificar un registro utilizando DALETE
command = "DALETE FROM Alumnos WHERE id = '004'"
cursor.execute(command)
connection.commit()
print("Numero de registros eliminados: ", cursor.rowcount)