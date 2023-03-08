#Posicion 0: un numero
#Posicion 1: un numero
#Posicion 2: un texto con la operacion a realizar -> sum, res, div, mul

def calcular(*num):
    result = None
    suma = ["suma"]
    resta = ["resta"]
    division = ["div"]
    multiplicación = ["mul"]

    try:
        if (num[2] in suma):
            result = (num[0] + num[1])
        if (calcular[2] = "res"):
            result = (num[0] - num[1])
        if (calcular[2] = "div"):
            result = (num[0] / num[1])
        if (calcular[2] = "mul"):
            result = (num[0] * num[1])
        else:
            raise = Exception 

def calcular(*num):
    for num in num:

