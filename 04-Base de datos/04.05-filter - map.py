numeros = [1, 85, 100, 200, 15]

def Proceasar(lista):
    resultado = []
    for numero in lista:
        resultado.append(numero * 10)

    return resultado

print(numeros)
print(Proceasar(numeros))

print(list(map(lambda x: x*10, numeros)))
print(list(map(lambda x: f"{x} x 10 = {x*10}", numeros)))
print(list(map(lambda x: x*10 , filter(lambda x: x > 100, numeros))))
print(list(filter(lambda x: x > 10 , map(lambda x: x*100, numeros))))