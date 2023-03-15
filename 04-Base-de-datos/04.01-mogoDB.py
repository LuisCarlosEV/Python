from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

#Crear el objeto que representa el cliente para trabajar con la base de datos
#Se requiere la cadena de conexion
client = MongoClient ("127.0.0.1", 27017)
    #client = MongoClient ("localhost", 27017)
    #client = MongoClient ("mongodb://localhost:27017")
    #client = MongoClient ("mongodb://127.0.0.1:27017")

##MOSTRAR EL ESTADO DEL SERVIDOR
# Nos posicionamos en una base de datos utilizando el objeto cliente

#db = client.admin

#Ejecutamos un comando sobre la base de datos
#Los comando nos permiten INSERTAR, ACTUALIZAR, ELIMINAR y LEER informacion de la base de datos

#El comando "serverStatus" nos retorna el estado del servidor en JSON
    #status = db.command("serverStatus")
    #pprint(status)
    #print(status)


#Listar 
print(client.list_database_names())


### Listar los nombres de la bases de datos
#Sintaxis Objeto
db = client.Northwind
print(db.list_collection_names())

#Sintaxis Coleccion
db2 = client["Northwind"]
print(db2.list_collection_names())

#Seleccionar una coleccion de la base de datos
collection = client.Northwind.Customers
    #collection = client["Northwind"]["Customers"]
    #collection = db.Customers
    #collection = db["Customers"]

#Mostrar el nuemero de documentos (registrados) en la coleccion
print(f"{collection.estimated_document_count()} documentos en {collection.name}")

#Leer datos
result = collection.find_one({"Country":"USA"})
print(result)
    #pprint(result)
result2 = collection.find({"Country":"USA"})
print(result2)

id = ObjectId("6409a5b722f2c7ff51ec47ef")
result3 = collection.find_one({"_id:": id})
result4 = collection.find_one({"_id:": ObjectId("6409a5b722f2c7ff51ec47ef")})
print(result4)