"""
Wortfrequenzanalyse
a. Lese einen Text ein und zähle, wie oft jedes Wort vorkommt
"""
from collections import Counter

SOME_TEXT = "Hallo, hallo mein Freund, wie geht es dir mein Freund?"

def _get_words(text):
    words = text.split()
    return words


def _clean_list(words_list):
    remove_chars = "!?,. "
    table = str.maketrans("", "", remove_chars)
    cleaned_list = []
    for word in words_list:
        cleaned_list.append(word.translate(table))
    return cleaned_list





words = _get_words(SOME_TEXT)
clean_list = _clean_list(words)
words_count = Counter(clean_list)

print(f"{words_count}:")
