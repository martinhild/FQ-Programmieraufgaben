"""
51. Einfacher BMI-Rechner
a. Lese Größe (in Metern) und Gewicht (in kg) ein und berechne den
BMI (Gewicht ÷ (Größe²)).
b. Gib das Ergebnis aus, z. B. mit zwei Nachkommastellen.
"""
from utils.user_inputs import get_float

print("Größe: ", end="")
size = get_float()
print("Gewicht: ", end="")
weight = get_float()

bmi = weight / size**2
print(f"BMI: {bmi:.2f}")
