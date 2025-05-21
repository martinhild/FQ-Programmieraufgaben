"""
Obst-Array
a. Lege ein Array mit Strings an (z. B. „Apfel“, „Banane“, „Kirsche“...). Frage den
Nutzer, nach welchem Obst er sucht, und gib aus, ob es im Array vorhanden ist
"""

obst = ["Apfel", "Banane", "Kirsche", "Birne"]
suche = input("Obst: ")
answer = "Vorhanden" if suche in obst else "Nicht vorhanden"
print(answer)