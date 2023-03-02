num1 = 0
num2 = 100

print("Inicio")

#num3 = num2 / num1
#print(f"Resultado: {num3}")

#f = open ('myfile.txt')

try: 
    #raise Exception("Mi error") #provoca el error y lleva directamente a except
    num3 = num2 / num1
    print(f"Resultado: {num3}")
    f = open ('myfile.txt')
except ZeroDivisionError as err:
    print("Upssss!!!! no se puede dividir por cero")
    print(err)
    print(type(err))
except FileNotFoundError as err:
    print("Upssss!!!! no se encuentra el archivo")
    print(err)
    print(type(err))
except Exception as err:
    print("Upssss!!!! se ha producido un error")
    print(err)
    print(type(err))
else:
    print("Bloque ELSE") # Considerado demás, sobra
finally:
    print("Bloque FINALLY")

print("FIN")