"""
Liest eine Dezimalzahl ein und konvertiert sie in Binär- und Hexadezimal-Darstellung.
"""
from utils.user_inputs import get_number

print("\nEnter decimal number: ", end="")

num_dec = get_number()

print(f"Binär: {bin(num_dec)}")
print(f"Hexadecimal: {hex(num_dec)}")

