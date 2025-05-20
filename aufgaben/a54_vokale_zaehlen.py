"""
54. Vokale zählen
a. Lese einen String ein und zähle, wie viele Vokale (a, e, i, o, u – Groß/Klein) darin
vorkommen
"""

text = input("Text: ")
text.lower()

n = 0
for char in text:
    if char in "aeiou":
        n +=1
print(n)