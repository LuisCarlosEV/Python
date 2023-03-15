from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
productos = db.Products
pedidos = db.Orders

lista_productos = list(productos.find())

#print(lista_productos.get('PrductID'), '-' productos.get('PrductName')) for product in products


print("/n Stock 0 con filter")
cursor = productos.find({'UnitsInStock': '0'})
while(cursor.alive):
    target = cursor.next()
    print(f"{target['ProductName']}")

print("/n Stock 0 con filter")
products = list(productos.find)
stock0 = list(filter(lambda x: x['UnitsInstock']=='0', products))
for prod in stock0:
    print(prod['ProductName'])

stock = productos.find()
valor = 0
for product in stock:
    price = product['UnitPrice']
    quantity = 

stock_value = sum(map(lambda productos: int(productos["UnitsInStock"]) * float()))


query = [
    {'$match': {'UnitsInStock': {'$ne': '0'}}},
    {"$addFields":{
        "Price": {"$toDouble": "$UnitPrice"}
        "Stock": {"$toInt": "$UnitsInStock"}
    }},
    {"$group"{
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products": {"$sum": 1}
    }}
]

cursor = db.Customers.aggregate(query)