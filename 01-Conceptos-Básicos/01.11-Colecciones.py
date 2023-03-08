# Utilizamos [] para crear listas
vacia = []
citricos = ["narajana", "limon", "pomelo", "lima","mandarina"]
coches = {"audi", "seat", "citroen", }

#Mostrar el contenido de una lista
print(citricos)

# Mostrar el valor contenido en una posicion (2 = pomelo)
print(citricos[2])

# Mostrar el numero de valores que contiene la lista
print(len(citricos))

# Mostrar el numero de veces que tenemos un valor
print(citricos.count("sandia"))

# Modificar el valor de la posición 2 (modificar pomelo por fresa)
citricos[2] = "fresa"
print(citricos)
print(citricos[2])

#Añadir nuevos valores utiliando la función APPEND
citricos.append("manzana")
citricos.append("melon")

#Añadir un nuevo valor en la posicion con la funcion ISERT(index, value)
citricos.insert(1, "sandia")

#Añadir si el valor no existe
if("platano" not in citricos):
    citricos.append("platano")

#Añadir varios valores procedentes de una lista con EXTEND(values)
NuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
citricos.extend(NuevasFrutas)

#Eliminar un valor en base a la posicion utilizando POP(index)
citricos.pop(5)

#Eliminar un valor en base al valor utilizando REMOVE(value)
citricos.remove("naranja")

#Eliminar un valor si existe
if("sandia" in citricos):
    citricos.remove("sandia")

#Invertir el orden de los valores utilizando REVERSE
citricos.reverse()

#Ordenar los valores utilizando SORT
citricos.sort()
citricos-sort(reverse = True)

#Recorremos la lista mostrando los valores
for i in citricos:
    print(i)

for index in range(0 , len(citricos),1):
    print(f"{index}: {frutas[index]}")

# Copiar la lista
vacia = citricos.copy()

#Limpiar la lista
citricos.clear()
