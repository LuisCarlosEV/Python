import pymssql, time

# Establecer conexión con la base de datos
connection = pymssql.connect(
    server="host-sqlserver-eoi.database.windows.net", 
    user="Administrador", 
    password="azurePa$$w0rd",
    database="Northwind")

# Creamos un cursor para ejecutar comando en la base de datos

# Retorna Diccionarios
cursor = connection.cursor(as_dict=True)

cursor.execute("SELECT * FROM dbo.Customers WHERE CustomerID = 'DEMO1'")
for row in cursor.fetchall():
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}\n")

cursor.execute("UPDATE dbo.Customers SET ContactTitle = 'Propietario' WHERE CustomerID LIKE '%DE%'")

connection.commit()
print(f"Numero de filas modificadas:", cursor.rowcount)
print("")