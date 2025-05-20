"""
Kreisfläche berechnen
a. Lese einen Radius ein und berechne die Kreisfläche (π * r²).
b. Tipp: Du kannst Math.PI verwenden, falls du in C# programmierst.
"""
from math import pi

from utils.user_inputs import get_float

print("Radius: ", end="")
r = get_float()
A = r**2 * pi
print(f"Fläche: {A:.2f}")