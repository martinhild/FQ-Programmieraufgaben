"""
Suchwort in Satz finden
a. Lese einen Satz und ein Suchwort ein. Prüfe, ob das Suchwort im Satz enthalten ist (Case-Insensitive).
"""

sentence = input("Satz: ")
search = input("Suchwort: ")

sentence = sentence.lower()
search= search.lower()

words = sentence.split()

if search in words:
    print("Enthalten")
else:
    print("Nicht enthalten")

