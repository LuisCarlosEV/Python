valor = 0

while (valor < 5):
    valor = valor + 1 # equivalente a valor += 1
    if (valor ==2):
        break   
    print(f"El valor es {valor}.")

print("Fin del WHILE")
print ("")

# WHILE para una coleccion
citricos = ["narajana", "limon", "pomelo", "lima","mandarina"]
index = 0

while (index < len(citricos)):
    print(f"{citricos[index]}")
    index += 1
print("Fin del WHILE")


# WHILE con un ELSE
while (index < len(citricos)):
    print(f"{citricos[index]}")
    index += 1
else:
    print("Fin del ELSE")
print("Fin del WHILE")

""" while true: 
   sentencias
   if (condicion):
       break """