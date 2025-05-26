"""
Suchen und Ersetzen in einer Datei
Öffne eine Textdatei, ersetze alle Vorkommen eines bestimmten Wortes durch
ein anderes.
"""

import re

PATH = "../data/suchen_und_ersetzen/beispiel.txt"


def read():
    """Liest Text und gibt ihn als Liste zurück"""
    with open(PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
        print("")
    return lines

def exchange(lines, old_word, new_word):
    """Ersetzt ein Wort mit einem anderen Wort im gesamten Text"""
    new_lines = []
    for line in lines:
        # Wort Ersetzen
        new_text = re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, line)
        new_lines.append(new_text)
    return new_lines


def main():
    lines = read()  # Lese den Inhalt der Datei
    print("Welches Wort ersetzen?")
    old_word = input("Altes Wort: ")
    new_word = input(f"{old_word} übersetzen in: ")

    # Ersetze das Wort in den Zeilen
    new_lines = exchange(lines, old_word, new_word)

    # Ausgabe des neuen Textes
    print("\nBearbeiteter Text:")
    for line in new_lines:
        print(line, end="")


if __name__ == '__main__':
    main()
