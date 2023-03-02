from datetime import datetime
import time

t1 = time.time()
t2 = time.localtime (t1)
t3 = time.asctime(t2)           #datime.srtfdate(datime.now(), "%c")

print(t1)
print(t2)
print(t2.tm_year)
print(t3)


############################# Fecha actual
print(" ")
dt1 = datetime.now().date()
print("Fecha 1", dt1)
print("Dia:", dt1.day)


########################### Hora actual
dt2 = datetime.now()
print(f"Fecha 2: {dt2}")
print("Dia:", dt2.day)
print("Hora:", dt2.hour)
print("Minuto:", dt2.minute)
print("Segundos:", dt2.second)
print("Milisegundos:", dt2.microsecond)

################## Formato fecha
strFecha = input("escribe tu fecha de nacimineto: ")
dt3 = datetime.strptime(strFecha, "%d-%m-%Y").date()

print(f"fecha de nacimiento: {dt3}")
print("fecha de nacimiento:", dt3.strftime("%C"))

#################### Edad
print(f"Tienes {dt1.year-dt3.year} años")

dias = dt1 - dt3
print(f"Tienes {dias} dias")