"""
Kleine Tabellen-Reihe
a. Frage den Nutzer nach einer Zahl. Gib anschließend diese kleine Reihe aus, z. B.
n, n², n³.
b. Beispiel: Zahl = 4 → Ausgabe: 4, 16, 64.
"""
from utils.user_inputs import get_number

print("Zahl: ", end="")
a = get_number()
print(a, a**2, a**3)
