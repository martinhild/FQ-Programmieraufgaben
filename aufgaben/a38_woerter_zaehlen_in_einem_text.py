"""
Lese einen Text (z. B. von der Konsole oder Datei) ein und zähle die Wörter.
"""

def clean_line(text):
    for zeichen in ".!?:,":
        text = text.replace(zeichen, "")
    return text

def count_words(text):
    words = text.split()
    return len(words)

with open("../data/Textdokument.txt","r") as file:
    count = 0
    for line in file:
        line = clean_line(line)
        count += count_words(line)

print(f"Words: {count}")


