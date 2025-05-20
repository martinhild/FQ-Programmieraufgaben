"""
Lege ein Dictionary/HashMap an, fülle es mit ein paar Schlüssel-Wert-Paaren (z.
B. Englisch–Deutsch) und frage Werte ab.
"""

def _get_dict():
    """ Returns a dictionary with user inputs. """
    print("Elemente eingeben. Drücke X zum Speichern.")
    dictionary ={}
    while True:
        german = input("Deutsch: ")
        if german in "xX":
            break
        english = input("Englisch: ")
        if english in "xX":
            break
        dictionary[german] = english
    return dictionary

def translate(dic):
    print("Gebe deutsche oder englische Wörter zum Übersetzen ein.")
    print("X zum Beenden.")
    while True:
        word = input("Welches Wort willst du übersetzen?\n")
        if word in "xX":
            break

        if word in dic:
            print(f"-> {dic[word]}")
        elif word in dic.values():
            for key, value in dic.items():
                if value == word:
                    print(f"-> {key}")
                    break
        else:
            print("-> Nicht gefunden / not found")


def main():
    dictionary = _get_dict()
    # dictionary = translations
    translate(dictionary)

if __name__=="__main__":
    main()