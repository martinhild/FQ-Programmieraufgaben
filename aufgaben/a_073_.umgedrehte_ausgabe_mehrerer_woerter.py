"""
Umgedrehte Ausgabe mehrerer Wörter
a. Lese eine Liste von Wörtern (z. B. 5 Stück) ein und gib sie in umgedrehter Reihenfolge (der Eingabe) wieder aus.
"""
ANZAHL = 3

words = [input(f"Word {i}: ") for i in range(1,ANZAHL+1)]

print("")

for word in words[::-1]: #[start, stop, step]
    print(word)