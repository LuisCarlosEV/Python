for x in range (10,0,-1):
    print(f"Número {x}")
print ("")

citricos = ["narajana", "limon", "pomelo", "lima","mandarina"]
print (citricos)
print (citricos[3])
print (f"Numero de valores: {len(citricos)}")
print ("")

for x in range(0,4,1):
    print  (f"{x} : {citricos[x]}")
print("")

for x in range(0,len(citricos),1):
    print  (f"{x} : {citricos[x]}")
print("")

for x in range(len(citricos)):
    print  (f"{x} > {citricos[x]}")
print("")

for x in citricos:
    print  (f"{x}")
print("")

for x in range (0,20,1):
    print(f"Número {x} - Inicio")
    if (x == 10):
        continue
    print(f"Número {x} - Fin")
print ("")

for x in range (0,20,1):
    print(f"Número {x} - Inicio")
    if (x == 10):
        break
    print(f"Número {x} - Fin")
print ("")