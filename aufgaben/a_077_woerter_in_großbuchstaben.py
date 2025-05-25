"""
Wörter in Großbuchstaben
a. Lese x Wörter ein, speichere sie in einem Array. Forme sie anschließend in Großbuchstaben um und gib sie aus.
"""

X = 4

words = [input(f"Wort {i+1}: ") for i in range(X)]

words = [word.upper() for word in words]

print(words)
