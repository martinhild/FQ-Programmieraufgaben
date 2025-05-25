"""
Benutzerdefinierte Funktion
a. Definiere eine eigene Funktion, die z. B. zwei Strings vergleicht und bei Gleichheit
true zurückgibt
"""

def _compare_strings(str1, str2):
    return str1==str2

text_1 = "affe"
text_2 = "affe"

if _compare_strings(text_1, text_2):
    answer = "gleich."
else:
    answer = "unterschiedlich."

print(f"\nDie Strings sind {answer}")
