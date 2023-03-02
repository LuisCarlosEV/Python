########################################################
# Conversiones                                         #
########################################################
#                                                      #
# Sintaxis: [nombre de la variable] = [valor inicial]  #
#                                                      #
# Ejemplos:                                            #
#         numero = 20                                  #
#         saludo = "Hola Mundo !!!"                    #
#                                                      #
########################################################

a = 5
b = "25"
c = "25.7"
temp = "hola"

print("Número: " + str(a))
print(b)
print(type(b))

print("")
print(int(b))
print(type((int(b))))

print("")
print(b+c)
print(int(b) + float(c))
print(type(int(b) + float(c)))

print("")
print(int(b) + int(float(c)))
print(type(int(b) + int(float(c))))