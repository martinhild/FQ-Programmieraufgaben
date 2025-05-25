"""
Zahlen-Reihung
a. Frage den Nutzer nach einem Start- und einem Endwert. Gib alle Zahlen von Start
bis Ende aus (aufsteigend, inkl. Grenzen).
b. Beispiel: Start=3, Ende=7 → Ausgabe: 3,4,5,6,7.
"""
from utils.user_inputs import get_number
print("Start=", end="")
start= get_number()
print("Ende=", end="")
end = get_number()

row = []
for i in range(start, end+1):
    row.append(i)
    row.append(",")
row.pop()

print("Ausgabe: ",end="")
for n in row:
    print(f"{n}",end="")