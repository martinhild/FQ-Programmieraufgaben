"""
Rechnen mit Potenzen
a. Lese eine Basis (b) und einen Exponenten (e) ein und berechne b^e. Falls e
negativ ist, weise darauf hin oder lass negative Exponenten aus.
"""
from utils.user_inputs import get_numbers

b, e = get_numbers("Basis: ", "Exponent: ")
ergebnis = b**e
if e < 0:
    print("Exponent negativ -> b**-e = 1/b**e")
print(ergebnis)