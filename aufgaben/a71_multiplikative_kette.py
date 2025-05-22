"""
Multiplikative Kette
a. Lese Zahlen ein, solange sie positiv sind. Multipliziere alle, bis du auf eine Null oder negative Zahl stößt. Gib dann das Produkt aus.
"""
from utils.user_inputs import get_number

print("Zahl eingeben. 0 oder negative zum beenden")

def _get_number():
    product = 1
    while True:
        try:
            n = int(input("Zahl: "))
            if n <= 0:
                break
            else:
                product *= n
        except ValueError:
            print("Muss ganzzahl sein.")

    return product

print(_get_number())

