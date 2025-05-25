"""
Zahl einbetten
a. Lese eine ganze Zahl ein. Erzeuge eine Zeichenkette, in der diese
Zahl „links und rechts“ eingerahmt ist, z. B.: --- 42 ---.
"""
from utils.user_inputs import get_number

number = get_number("Ganzzahl: ")
text =f"--- {number} ---"
print(text)