numeros = []

#equivalente a filter()
def filtrado(formula,datos):
    resultado=[]
    for x in datos:
        if(formula(x) == True):
            resultado.append(x)
    return resultado

print(">>>", filtrado(lambda x: x > 100, numeros))