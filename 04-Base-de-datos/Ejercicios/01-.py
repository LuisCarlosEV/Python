#Definir la conexion

#Cuantos productos tenemos ?? buscamos en Mongo DB
#Mostramos el nuemro de productos y un listado

#Filtrar los productos con UnitsInStock , utilizando filter()

#Valor del stock UnitsInStock x UnitPrice
## Una forma: Con un for 
## Otra forma: con un MAP () Sum()
## con una funcion aggregate de mongoDB y los operadores $sum y $multiply

#Con un identificador de pedido
##Mostramos los datos de entrega --> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
##Mostramos el detalle del pedido --> Procudto, Cantidad, Precio, Precio Total, Total Pedido
texto = "Ejemplo"
print(f"{'Producto':<30} {texto:>10}")

from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client = MongoClient ("mongodb://localhost:27017")
db = client.Northwind
productos = db.Products
pedidos = db.Orders

print(db.list_collection_names())
print(f"{productos.estimated_document_count()} documentos en {productos.name}")
print(f"Numero de documentos sin filtrar: {productos.estimated_document_count()}")

for index in db.Product.list_indexes():
    print(index)

#cursor = productos.find({})
#while (cursor.alive):
    #producto = cursor.next()



