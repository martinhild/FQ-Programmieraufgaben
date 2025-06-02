"""
Rekursive Funktionen
Implementiere eine rekursive Funktion, die z. B. die Tiefe eines
Verzeichnisbaums ausgibt (oder simpler: die Summe von 1 bis n).

b) Die Tiefe eines Verzeichnisbaums:
"""

"""
    Pseudocode:
    
    Funktion(Pfad):
        max_tiefe = 0
        Für jeden Inhalt im jetzigen Pfad:
            Erweiterter_Pfad = Pfad + Inhalt
            Wenn Erweiterter_Pfad ein Directory ist: # Basisfall: kein Directory mehr da
                Tiefe = Funktion(erweiterter_pfad)   # Rekursion (aktuell 1 + 0)
                Wenn Tiefe > max_tiefe:
                    max_tiefe = tiefe
        return 1 + max_tiefe
"""

import os


from utils.user_inputs import get_path


def func(path):
    """
    Berechnet rekursiv die Tiefe eines Verzeichnisbaums.
    """
    max_depth = 0
    for item in os.listdir(path):
        extended_path = os.path.join(path,item)  # -> path/item
        if os.path.isdir(extended_path):
            depth = func(extended_path)  # recursion
            if depth > max_depth:
                max_depth = depth
    return 1 + max_depth


def main():
    path_user_input = get_path()
    max_depth_of_tree = func(path_user_input)
    direct = os.path.basename(path_user_input)

    print(f"\nDas Directory:   {direct}\nim Verzeichnis:  {path_user_input}"
          f"\nhat eine maximale Tiefe von:  {max_depth_of_tree}")


if __name__ == '__main__':
    main()