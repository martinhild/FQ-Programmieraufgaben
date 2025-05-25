"""
Lese einen Text (z. B. von der Konsole oder Datei) ein und zähle die Wörter.
"""

def _clean_line(text):
    for zeichen in ".!?:,":
        text = text.replace(zeichen, "")
    return text

def _count_words(text):
    words = text.split()
    return len(words)

with open("../data/encryption/caesar_chiffre.txt", "r") as file:
    count = 0
    for line in file:
        line = _clean_line(line)
        count += _count_words(line)

print(f"Words: {count}")


