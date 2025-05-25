"""
Datum und Zeit
Lese das aktuelle Datum aus dem System, formatiere es in verschiedenen
Formaten und gib es aus.
"""
from datetime import datetime

now = datetime.now()

date = now.strftime("%d.%m.%Y")
print(date)
date = now.strftime("%d.%m.%y")
print(date)
date = now.strftime("%d-%m-%y")
print(date)
date = now.strftime("%m/%d/%y")
print(date)

time = now.strftime("%H:%M:%S")
print(time)
time = now.strftime("%I:%M:%S %p")
print(time)