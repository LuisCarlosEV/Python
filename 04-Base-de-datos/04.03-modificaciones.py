from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

query = {"Country": "USA"}
newValues = {
    "$set" : {
    "Country": "Estados Unidos",
    }
}

print(collection.count_documents(query), "Clientes USA")
result = collection._update
print(result.modified_count, "documentos modificados")
print(result)
print(collection.find_one(query))

exit()
documento = collection.find_one(query)
pprint(documento)


newValues = {
    "$set" : {
    "Address": "Calle Serrano",
    "PostalCode": "28045",
    "Phone":"912002022",
    }
}

result = collection.update_one(query, newValues)
print(result.matched_count, "documentos encontrados")
print(result.modified_count, "documentos modificados")
print(result)
print(collection.find_one(query))