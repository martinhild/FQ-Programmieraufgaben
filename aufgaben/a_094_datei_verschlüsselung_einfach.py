"""
Datei-Verschlüsselung (einfach)
a. Lies den Inhalt einer Datei aus, verschlüssele ihn einfach
(z. B. Caesar-Chiffre) und speichere ihn wieder
"""

PATH = "../data/encryption/caesar_chiffre.txt"
KEY = -4


def print_file(path):
    """Ausgabe des Inhalts der Datei zeilenweise."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line,end="")


def caesar_chiffre(text, key):
    """
    Verschlüsselt Text durch Caesar-Chiffre mit Schlüssel KEY (Verschiebung).
    Nur Buchstaben werden verschoben.
    """
    text_encrypted = ""
    for char in text:

        # Wenn char ein Buchstabe ist
        if char.isascii() and char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            new_ascii = (ord(char) - offset + key) % 26
            text_encrypted += chr(new_ascii + offset)
        else:
            text_encrypted += char  # Nicht-Buchstaben bleiben
    return text_encrypted


def encrypt():
    """
    Liest Datei ein, speichert Text Zeilenweise in einer Liste und
    verschlüsselt diesen mit caesar_chiffre(). Abschließend wird die
    Datei überschrieben.
    """
    # Einlesen
    with open(PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Zeilenweise verschlüsseln
    new_lines = []
    for line in lines:
        new_line = caesar_chiffre(line, KEY)
        new_lines.append(new_line)

    # File überschreiben
    with open(PATH, "w", encoding="utf-8") as file:
        file.writelines(new_lines)


def main():
    print_file(PATH)
    encrypt()
    print_file(PATH)


if __name__ == "__main__":
    main()


# python -m flake8 a94_datei_verschlüsselung_einfach.py
