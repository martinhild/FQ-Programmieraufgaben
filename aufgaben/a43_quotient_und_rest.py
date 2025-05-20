"""
a. Lese zwei ganze Zahlen ein und berechne zum einen den ganzzahligen
Quotienten (Division) und zum anderen den Rest (Modulo).
b. Beispiel: 17 ÷ 5 → Quotient 3, Rest 2.
"""
from utils.user_inputs import get_numbers

a, b = get_numbers()
ganz_quot = a//b
rest = a % b
print(f"{ganz_quot} Rest {rest}")