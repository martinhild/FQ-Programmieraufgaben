"""
Kilobyte zu Megabyte
a. Lese einen Wert in Kilobyte ein und rechne ihn in Megabyte um (1 MB = 1024 KB).
b. Gib das Ergebnis z. B. mit drei Nachkommastellen aus.
"""
from utils.user_inputs import get_number

kb = get_number("MB: ")
mb = 1024 * kb
print(f"{mb:.3f} KB")