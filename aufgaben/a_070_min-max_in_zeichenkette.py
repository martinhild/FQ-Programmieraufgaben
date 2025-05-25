"""
Min-Max in Zeichenkette
a. Lese eine Zeichenkette ein. Finde das „alphabetisch kleinste“ und „alphabetisch größte“ Zeichen (z. B. a < b < … < z).
"""

text = input("Text: ")

min = max = text[0]
for char in text:
    if ord(char) < ord(min):
        min = char
    if ord(char) > ord(max):
        max = char

print(min,max)
