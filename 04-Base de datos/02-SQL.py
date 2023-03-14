import pymssql, time

#Establecer la conexion
connection = pymssql.connect(
    server = "host-sqlserver-eoi.database.windows.net",
    user = "Administrador",
    password = "azurePa$$w0rd",
    database = "Northwind"
)

#Creamos cursor
#Retorna Tupla
cursor = connection.cursor()

#Retornar diccionario
cursor = connection.cursor(as_dict = True )


#Insertamos con el comando INSERT
cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES ('DEM56', 'Comidas 1 2 3, SL', 'Borja Cabeza', 'Madrid', 'Spain')")
connection.commit()


command = "INSERT INTO dbo.Customers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
command = "INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES (%d, %d, %d, %d, %d, %d, %d, %d, "

data = []
data.append(('DEA10', 'Empresa Uno SL', 'Madrid', 'Spain'))
data.append(('DEA20', 'Empresa dos SL', 'Madrid', 'Spain'))
data.append(('DEA30', 'Empresa tres SL', 'Madrid', 'Spain'))



#Utilizamos la funcion commit() para confirmar la transacion y las operaciones de insercion
#actualizacion y borrado
connection.commit()

#Utilizamos la funcion rollback() para cancelar la transacion y las operaciones de insercion
#insercion, actualizacion y borrado
###connection.rollback()


exit()
#Ejemplos de SELECT, para retornar registros
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'SPAIN' ORDER BY City")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")

pais = "Spain"
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", pais)

cursor.execute("SELECT CustomerID, CompanyName, Country, City FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")
cursor.execute("SELECT * FROM dbo.Customers ORDER BY City")

#cronometro para comparar FOR y WHILE
##timea = time.perf_counter()

#Mostramos el contenido con un FOR
for row in cursor.fetchall():
    print(f"ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}")
    
    #En caso de tuplas se usa posiciones
    ##print(f"ID: {row[0]}")
    ##print(f"Empresa: {row[1]}")

#cronometro para comparar FOR y WHILE
##timeb = time.perf_counter() - timea
##print(f"{timeb:0.10f}")

#Mostramos el contenido mediante un WHILE
row = cursor.fetchone()
while(row):
    print(f"ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}")
    row = cursor.fetchone()

#cronometro para comparar FOR y WHILE
##timec = time.perf_counter() - timea
##print(f"{timec:0.10f}")