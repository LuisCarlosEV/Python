from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

result = collection.delete_many({"CustomerID": {"$regex":"DEMO"}})
print(f"{result.deleted_count} documentos eliminados")
print(f"{collection.count_documents({'CustomerID': {'$regex': 'DEMO'}})} clientes DEMO")

result = collection.delete_one({"CustomerID": "DEMO1"})
print(f"{result.deleted_count} documentos eliminados")
print(result)

collection.distinct