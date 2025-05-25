"""
Zahlensumme mit Abbruch
a. Lese fortlaufend Zahlen ein und rechne sie zusammen. Sobald eine negative Zahl
eingegeben wird, brich ab und gib die Summe aller zuvor eingegebenen (nicht-
negativen) Zahlen aus.
"""
from utils.user_inputs import get_number

total = 0
print("Enter whole Numbers, negative ones to quit")
while True:
    n = get_number()
    if n < 0:
        break
    total += n
print(f"Summe: {total}")
