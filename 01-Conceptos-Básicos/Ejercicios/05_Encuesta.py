#######################################################################
# Requerimientos funcionales:
#   
#   -> Visualizar la media de opinión 
#   -> Visualizar el número total de encuentas
#   -> El resultado se muestra al escribit FIN
#   -> El valor de opión es entre 0 y 10
#######################################################################
# Utilizando listas de Python
#######################################################################

encuesta = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
opinion = 0

print(f"numero de encuestas: {len(encuesta)}")

media = sum(encuesta) / len(encuesta)

print(media)

while (opinion < len(encuesta)):
    opinion += 1

try:
    resultado = input("Escribir FIN para obtener el resultado: ")
    if (resultado != "FIN"):
        print("FIN mal escrito")
    else:
        print(media)
except:
    print("Encuestas no validas")             