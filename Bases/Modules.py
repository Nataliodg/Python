#PRIMERA OPCIÓN (IMPORTAR TODO EL MODULO):
# import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes=70))

#SEGUNDA OPCIÓN (IMPORTAR LO QUE SE NECESITA):
from datetime import timedelta, date

print(timedelta(minutes=70))
print(date.today())


