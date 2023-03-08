################################################################################################################
# Requerimientos funcionales:
#
# -> Calcular la edad: fecha actual - fecha de nacimiento
# -> Mostrar si es mayor de edad
# -> Si no es mayor de edad mostrar los años que le faltan para la mayoria de edad
# 
################################################################################################################

from datetime import datetime

today = datetime.now().date()
strFecha = input("Escribe tu fecha de nacimineto (dd/mm/yyyy): ")
try:
    birthday = datetime.strptime(strFecha, "%d-%m-%Y").date()
    print(f"Tienes {today.year-birthday.year} años")
    print("")

    if (today.year-birthday.year > 18):
        print("Eres mayor de edad")
    else:
        print(f"te faltan {18-(today.year-birthday.year)} años")
except:
    print("No se puede calcular porque el formato de fecha no es valido")


