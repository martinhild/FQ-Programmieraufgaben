"""
Entferne alle Ziffern aus String
a. Lese einen String mit Buchstaben und Zahlen ein. Entferne alle Ziffern und gib nur die Buchstaben-/Satzzeichenfolge zurück.
"""
import re

text = input("Text: ")

new = re.sub(r'[0-9]',"",text)
print(new)


