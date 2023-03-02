from datetime import datetime, timedelta, timezone
from pytz import timezone
import pytz

#mostrar zonas horarias
#print(pytz.all_timezones)
#print(type(pytz.all_timezones))

#mostrar fecha actual
dt = datetime.now()
print(dt)

print("")

print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("Europe/Madrid")))
print(datetime.now(pytz.timezone("US/Alaska")))
print(datetime.now(pytz.timezone("UTC")))
print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("America/Bogota")))