"""
Lese zwei Zahlen ein und gib deren Differenz aus (erste minus zweite).
Beispiel: Eingaben 10 und 3 → Ausgabe 7.
"""
from utils.user_inputs import get_numbers

a, b = get_numbers()
print(f"Differenz: {a-b}")
