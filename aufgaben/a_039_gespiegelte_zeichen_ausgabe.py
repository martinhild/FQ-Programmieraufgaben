"""
Lese ein Wort ein und ersetze jeden Buchstaben mit seinem „gespiegelten“
Alphabetpartner (z. B. A↔Z, B↔Y usw.).
"""
LETTERS = 26 # size of alphabet
OFFSET = {'A':65, 'a':97}
"""
65   A       97    a
66   B       98    b
67   C       99    c
...          ...
"""

def mirror_letter(letter):
    ascii_num = ord(letter)
    if 'A' <= letter <= 'Z': # A-Z
        offset = OFFSET['A']
    elif 'a' <= letter <= 'z': # a-z
        offset = OFFSET['a']
    else:
        return letter
    mirrored_letter = chr((LETTERS - 1 - (ascii_num - offset)) + offset)
    # (ascii_num - offset): Position im Alphabet (A=0, B=1, ...)
    # (LETTERS - 1 - ...): Spiegelung
    #  ... + offset: zurück zum richtigen ASCII-Wert
    return mirrored_letter

def mirror_word(old_word):
    new_word = ""
    for char in old_word:
        letter = mirror_letter(char)
        new_word += letter
    return new_word

def main():
    word = input("Wort: ")
    word = mirror_word(word)
    print(word)

if __name__ == "__main__":
    main()

