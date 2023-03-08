#######################################################################
# Requerimientos funcionales:
#
#   -> Calcular la letra de DNI
#   -> Formular: dni % 23
#######################################################################

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

try:
    numero = input("Introduzca su número del DNI (8 digitos): ")
    if(len(numero)!=8):
        print("El DNI no tiene 8 digitos")
    else:    
        n = int(numero)
        letraDNI = letras [n%23]
        print(letraDNI)
except:
    print("Número del DNI escrito incorrectamente")    
