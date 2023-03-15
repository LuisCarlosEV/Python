from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Country = None
    PostalCode = None
    Region = None
    Phone = None
    Fax = None

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

cliente = Customer()
cliente.CustomerID = "DEMO10"
cliente.CompanyName = "Un dos trs Bebidas, SL"
cliente.ContactName = "Borja"
cliente.ContactTitle = "Propietario"
cliente.Address = "Gran via"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "Spain"
cliente.PostalCode = "28044"
cliente.Phone = "912002020"
cliente.Fax = "912002020"

print(cliente.__dict__)

resultado = collection.insert_one(cliente.__dict__).inserted_id
print(f"ID: {resultado}")

exit()
#id = input("Escribe el ID del cliente: ")

cliente = {
    "CustomerID": id,
    "CompanyName": "Uno Comida SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía, 42",
    "City": "Madrid",
    "Country": "Spain",
    "PostalCode": "28044",
    "Region":"Madrid",
    "Phone":"912002020",
    "Fax":"912002020",
    }

#Comienza por DEMO

#Acaba en DEMO

#Contiene DEMO
cursor = collection.find({"CustomerID": {"$regex": "DEMO"}})
cursor = collection.find({"CustomerID": "/DEMO.*/"})
while(cursor.alive):
    doc = cursor.next()
    print(f"{doc['CustomerID']}# {doc['CompanyName']}")



exit()
id = collection.insert_one


exit()
resultado = collection.insert_one(cliente)
print(f"Resultado: {resultado}")
print(f"Resultado: {resultado.inserted_id}")
print(f"Resultado: {resultado.acknowledged}")