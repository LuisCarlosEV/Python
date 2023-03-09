from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

cursor = collection.find({"Country":"USA"})
cursor = collection.find({"Country":"USA"}).limit(3)
cursor = collection.find({"Country":"USA"}).skip(5)
cursor = collection.find({"Country":"USA"}).sort("City")     #Ascendente A --> W
cursor = collection.find({"Country":"USA"}).sort("City",1)   #Ascendente A --> W
cursor = collection.find({"Country":"USA"}).sort("City",-1)  #Descendente W --> A
cursor = collection.find({"Country":"USA"}).sort("City",-1).limit (3)

while (cursor.alive):
    document = cursor.next()
    print(document["CompanyName"]), document["Country"], document["City"]
    print("")

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

