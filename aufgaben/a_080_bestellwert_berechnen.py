"""
Bestellwert berechnen
a. Frage nach Anzahl und Einzelpreis eines Produkts und berechne den Gesamtpreis. Falls Anzahl über 100 ist, gewähre einen Rabatt von 5%.
"""
from utils.user_inputs import get_number, get_float

number = get_number("Anzahl: ")
unit_price = get_float("Einzelpreis: ")
discount = 0.95 if number > 100 else 1
total_price = number * unit_price * discount

print(f"Fesamtpreis: {total_price:.2f} €")