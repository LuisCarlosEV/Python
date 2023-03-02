########################################################
# Asignación simultánea                                #
########################################################
#                                                      #
# Sintaxis: [nombre de la variable] = [valor inicial]  #
#                                                      #
# Ejemplos:                                            #
#         numero = 20                                  #
#         saludo = "Hola Mundo !!!"                    #
#                                                      #
########################################################

#Cambiar los valores de a y b. Intento 1.
a=5
b=10

a=b
b=a

print("Intento 1. Forma incorrecta")
print(a)
print(b)
print("")

#Cambiar los valores de a y b. Intento 2.
a=5
b=10

temp=a
a=b
b=temp

print("Intento 2. Forma correcta - Funciona")
print(a)
print(b)
print("")

#Cambiar los valores de a y b. Intento 3.
a=5
b=10

a,b = b,a

print("Intento 3. Forma correcta - Funciona - Idóneo en Pythin")
print(a)
print(b)
print("")