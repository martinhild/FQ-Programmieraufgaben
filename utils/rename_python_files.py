import os
import re
"""
wandelt py files die mit einer Zahl anfangen um in "aZahl"
"""
# Arbeitsverzeichnis
verzeichnis = "../aufgaben"

for dateiname in os.listdir(verzeichnis):
    if dateiname.endswith(".py") and re.match(r"^\d", dateiname):
        neuer_name = "a" + dateiname
        alter_pfad = os.path.join(verzeichnis, dateiname)
        neuer_pfad = os.path.join(verzeichnis, neuer_name)
        os.rename(alter_pfad, neuer_pfad)
        print(f"{dateiname} -> {neuer_name}")