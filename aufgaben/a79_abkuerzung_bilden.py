"""
Abkürzung bilden
a. Lese einen Satz ein (z. B. „Fachhochschule für Technik“) und bilde eine Abkürzung aus den Anfangsbuchstaben aller Wörter (z. B. „FFT“).
"""

sentence = input()
list_sentence = sentence.split()

short = ""
for word in list_sentence:
    short += word[0].upper()
print(short)