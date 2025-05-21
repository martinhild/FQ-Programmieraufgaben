"""
Höhe eines Dreiecks
a. Lese Grundseite und Fläche eines Dreiecks ein, berechne die Höhe (Formel:
Höhe = (2 × Fläche) / Grundseite)
"""
from utils.user_inputs import get_float

g = get_float("Grundseite: ")
h = get_float("Höhe: ")

flaeche = 0.5 * g * h

print(f"Fläche: {flaeche}")