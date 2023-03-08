################################################################################################################
# Requerimientos funcionales:
#
# -> Calcular la velocidad en km/h
# -> La información la tenemos en metros y minutos (input)
# -> Diferenciar entre ALTA> 75 km/h; Baja < 30km/h; el resto moderada
# 
################################################################################################################

try:
    #Input de los metros y minutos
    velocidad_metros = int(input("Pon la distancias en metros: "))
    velocidad_segundos = int(input ("Pon el tiempo en minutos: "))

    #transformar los metros a km
    velocidad_km = velocidad_metros /1000

    #transformar los segundos a horas
    velocidad_horas = velocidad_segundos /3600

    print(f"velocidad es: {velocidad_km/velocidad_horas} km/h")

    if(velocidad_km/velocidad_horas>75):
        print("Velocidad ALTA")
    if(velocidad_km/velocidad_horas<30):
        print("Velocidad BAJA")
    else:
        print("Velocidad MODERADA")

except:
    print("Metros o minutos introducidos incorrectamente")
    exit()