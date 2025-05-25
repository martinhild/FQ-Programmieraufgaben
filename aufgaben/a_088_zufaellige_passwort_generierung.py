"""
Zufällige Passwort-Generierung
a. Erzeuge ein zufälliges Passwort einer bestimmten Länge mit Buchstaben, Zahlen
und Sonderzeichen.
"""

# Bereich	Beschreibung	ASCII	Beispiele
# 48–57	    Ziffern	        0–9	    0 1 2 3 4 5 6 7 8 9
# 65–90	    Großbuchstaben	A–Z	    A B C ... Z
# 97–122	Kleinbuchstaben	a–z	    a b c ... z
# 33–47	    Sonderzeichen		    ! " # $ % & ' ( ) * + , - . /
# 58–64	    Sonderzeichen           : ; < = > ? @
# 91–96	    Sonderzeichen		    `[ \" ] ^ _ ``
# 123–126	Sonderzeichen		    `{

import random

# 33-122
LENGTH = 14

def _rnd():
    n = random.randint(0,6)
    a = b = 0
    match n:
        case(0): a, b = 48, 57
        case(1): a, b = 65, 90
        case(2): a, b = 97, 122
        case(3): a, b = 33, 47
        case(4): a, b = 58, 64
        case(5): a, b = 91, 96
        case(6): a, b = 123, 126
    return random.randint(a, b)

def main():
    password = ""
    for _ in range(LENGTH):
        password += chr(_rnd())

    print(f"\nPasswort: {password}")

if __name__ == "__main__":
    main()
    