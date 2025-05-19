"""
Lese ein Wort ein und ersetze jeden Buchstaben mit seinem „gespiegelten“
Alphabetpartner (z. B. A↔Z, B↔Y usw.).
"""
LETTERS = 26 #size if alphabet

def new_ord(number):
    new_number = 25-number
    return new_number

x = int(input("Zahl: "))
x = x - 65
x = new_ord(x)
x = x + 65

print(x)

