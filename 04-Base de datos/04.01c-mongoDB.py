from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

#cursor = collection.find({"Country":"USA"})
#cursor = collection.find({"Country":"USA"}).limit(3)
#cursor = collection.find({"Country":"USA"}).skip(5)
#cursor = collection.find({"Country":"USA"}).sort("City")     #Ascendente A --> W
#cursor = collection.find({"Country":"USA"}).sort("City",1)   #Ascendente A --> W
#cursor = collection.find({"Country":"USA"}).sort("City",-1)  #Descendente W --> A
#cursor = collection.find({"Country":"USA"}).sort("City",-1).limit (3)

"""

===================================================

 Listado de operadores relacionales

===================================================

$eq - equal - igual

$lt - low than - menor que

$lte - low than equal - menor o igual que

$gt - greater than - mayor que

$gte - greater than equal - mayor o igual que

$ne - not equal - distinto

$in - in - dentro de

$nin - not in - no dentro de

"""

""" 
#Ambas consultas buscan clientes de USA (ambas son iguales)
cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": {"$eq" : "USA"}})

#Todos los clientes que no son de USA
cursor = collection.find({"Country": {"$ne" : "USA"}})

#Buscamos clientes de USA y Mexico
cursor = collection.find({"Country": {"$in" : ["USA","MExico"]}}).sort("Country")

#Buscamos clientes de USA y la ciudad de San Francisco
cursor = collection.find({"country": "USA", "City": "San Francisco"})
cursor = collection.find("$and": [{"country": "USA"}, {"City": "San Francisco"}])

#Ordenar por dos campos o mas
#Una consulta con dos campos y operador OR
cursor = collection.find("$or": [{"Country": "USA"}, {"Country": "Germany"}])


 """
collection2 = db.Orders

cursor = collection.find({"Country": "Mexico"})

while (cursor.alive):
    cliente = cursor.next()
    print(f"{cliente['CustomerID']} - {cliente['CompanyName']}")
    cursorPedidos = collection2.find({"Customer ID": cliente['CustomerID']})
    while (cursorPedidos.alive):
        pedido = cursorPedidos.next()
        print(f">>>> {pedido['OrderID']} - {pedido['OrderDate']}")

print("===========================================================================================")   

#Los datos de ANATR y todos sus pedidos

cursor = collection.aggregate([
    {"$match": {"CustomerID": "ANATR"}},
    {"$sort": {"City": 1}},
    {"$lookup": {
        "from": "Orders",
        "localField": "CustomerID",
        "foreingField": "CustomerID"
        "as": "Orders"
    }}
     
])

while (cursor.alive):
    customer = cursor.next()
    print(f"{customer['CustomerID']} - {customer['CompanyName']}")
    for pedido in customer["Orders"]:
        

exit()
#print(f"Nuemero de documento: {cursor.()}")
print("Nuemero de documentos filtrados:", collection.count_documents({"Country":"USA"}))
print(f"Nuemero de documentos sin filtrar: {collection.estimated_document_count()}")
print("Datos pendientes de leer:", cursor.alive)

    #while (cursor.alive):
    #    pprint(cursor.next())
    #    print("")
    #print("Datos pendientes de leer:", cursor.alive)

    #cursor = collection.find({"Country":"USA"})
    #for document in list(cursor):
    #    pprint(document)
    #    print("")

