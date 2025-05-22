"""
Summe gerader Stellen einer Zahl
a. Bilde die Summe der Ziffern auf den geraden Positionen einer eingegebenen
Zahl (z. B. 1234 → Positionen [von links]: 1=1, 2=2, 3=3, 4=4. Du entscheidest
selbst, ob du von links oder rechts zählst, aber gib die Logik an).
"""
from utils.user_inputs import get_number

number = str(get_number("Zahl: "))
numbers = list(number)

for i in range(1,len(numbers),2): print(numbers[i])
"""
for i in range( , , ): ... [i] ...
for i in range(1,len(numbers),2): print(numbers[i])
"""