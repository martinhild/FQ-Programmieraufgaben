import os
import re
"""
wandelt py files die mit einer Zahl anfangen um in "aZahl"
"""
# Arbeitsverzeichnis
verzeichnis = "../aufgaben"

for dateiname in os.listdir(verzeichnis):

    # Dateiname endet mit .py und beginnt mit a und einer Zahl
    if dateiname.endswith(".py") and re.match(r"^a\d", dateiname):

        # Neuer Dateiname
        neuer_name = dateiname[0] + "_" + dateiname[1:]
        alter_pfad = os.path.join(verzeichnis, dateiname)
        neuer_pfad = os.path.join(verzeichnis, neuer_name)
        os.rename(alter_pfad, neuer_pfad)
        print(f"{dateiname} -> {neuer_name}")