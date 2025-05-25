"""
Verschachtelte Schleifen
a. Erzeuge ein mehrdimensionales Muster (z. B. ein Rechteck aus Sternen mit
Rahmen)
"""

size = 8
zeile_gerade = True


print(" "+ "_" * 24 + " ")


for zeile in range(size):
    print("|", end="")  # Anfang

    for spalte in range(size):
        if zeile_gerade:
            if spalte % 2 == 0:
                print(" █ ", end="")
            else:
                print("   ", end="")
        else:
            if spalte % 2 == 1:
                print(" █ ", end="")
            else:
                print("   ", end="")
    print("|")  # Ende

    zeile_gerade = not zeile_gerade


print(" "+ "‾" * 24 + " ")
