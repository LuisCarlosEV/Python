
vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"líma", "MA":"mandarina"}

#Mostrar el diccionario
print(frutas)

#Mostrar un valor utilizando la clave
#Si la clave no exite se produce una Exception
print(frutas["NA"])

#Mostrar un valor utilizando la funcion GET
#Si la clave no exite la funcion GET retorna el valor None
print(frutas.get("NA"))
print(frutas.get("NI"))

#Mostrar el numero de valores del diccionario
print(len(frutas))

#Modificar un valor de un elemento
frutas["NA"] = "sandia"
frutas.update({"NA": "ciruela"})
print(frutas["NA"])


#Añadir un nuevo valor al diccionario
frutas["ME"] = "melon"
frutas.update({"KI": "kiwi"})
print(frutas)

#Eliminar valor utilizando la clave
frutas.pop("NA")
del frutas["LM"]
print(frutas)

#Recorremos con un FOR la lista
for key in frutas:
    print(f"Clave: {key} - Valor {frutas[key]}")
print(frutas)