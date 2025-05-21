"""
Anzahl der Stellen
a. Lese eine ganze Zahl ein und bestimme, wie viele Ziffern diese Zahl hat
(Vorzeichen zählt nicht mit).
b. Beispiel: -120 → 3 Ziffern.
"""
from utils.user_inputs import get_number, prompt

number = get_number("Number: ")
digits = len(str(abs(number)))

print(f"{digits}")