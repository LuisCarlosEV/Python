cadena = "   hola mundo!!!  "

print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[2:6])
print(cadena[:6])
print(cadena[-2])
print(len(cadena))

print("")
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o","0"))
print(cadena.isdigit())
print("57".isdigit())
print(cadena.count("a"))


mensaje = "mundo"

print("Hola " + mensaje + " !!")
print("Hola {} !!!".format (mensaje))
print("Hola {s} !!!".format (s=mensaje))
print("Hola {mensaje} !!!".format (mensaje))
print("Hola {mensaje} !!!")
print(f"Hola {mensaje} {cadena}!!!")

resultado = "Hola {s} !!!".format (s=mensaje)
print(resultado)

numero = 10/3
print(numero)
print("Numero: {n}".format(n=numero))
print("Numero: {n:1.2f}".format(n=numero))
print(type("Numero: {n:1.2f}".format(n=numero)))
