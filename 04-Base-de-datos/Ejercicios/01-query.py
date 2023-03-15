from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
collection = db.Products

query = [
    {"$match": { "UnitsInStock": {"$ne": "0"}}},
    {"$addFields": {
        "Price": {"$toDouble": "$UnitPrice"},
        "Stock": {"$toInt": "$UnitsInStock"}
    }},
    {"$group":{
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products": {"$sum": 1}
    }}
]

cursor = collection.aggregate(query)
print(cursor.next())