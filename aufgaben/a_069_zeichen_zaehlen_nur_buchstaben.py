"""
Zeichen zählen (nur Buchstaben)
a. Lese einen String ein und zähle nur die Buchstaben (A–Z, a–z), also ohne Leerzeichen, Zahlen, Satzzeichen.
"""
import re

text = input("Text: ")
clean_text = re.sub('[^A-Za-z]', "",text)
"""
- Das r vor dem String bedeutet Raw String, dadurch werden
  Backslashes \ nicht als Escape-Zeichen interpretiert.
-  [^...] bedeutet "KEIN Zeichen aus dieser Gruppe".
"""

# print(len(clean_text)) <- einfach

n = sum(1 for char in clean_text)
"""
Generator: (1 for char in clean_text) runde Klammern
Vgl List Comprehension: [ausdruck for element in iterable]
in eckigen Klammern
"""


print(n)




