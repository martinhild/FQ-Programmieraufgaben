"""
Binäre Suche
Erstelle ein sortiertes Array und implementiere eine binäre Suchfunktion nach
einem gesuchten Wert.
"""
from utils.user_inputs import get_number


def create_sorted_list(start, end):
    """
    Gibt eine sortierte Liste einer aufsteigender Zahlenreihe in wählbarem
    Bereich zurück.
    """
    sorted_list = [int(i) for i in range(start, end+1)]
    return sorted_list


def binary_search(target, lst):
    """
    Durchsucht eine Liste nach einer Zahl mit dem Binary-Search-Algorithmus.
    Gibt bei Erfolg den Index und bei Misserfolg -1 zurück.
    """
    index_start = 0
    index_end = len(lst) - 1

    while index_start <= index_end:
        index_mitte = (index_start + index_end) // 2

        # Ziel gefunden
        if target == lst[index_mitte]:
            return index_mitte

        # Ziel links von index_mitte
        elif target < lst[index_mitte]:
            index_end = index_mitte - 1

        # Ziel rechts von index_mitte
        elif target > lst[index_mitte]:
            index_start = index_mitte + 1

    # Ziel nicht gefunden
    return -1


def main():
    start = get_number("\nStart: ")
    end = get_number("Ende: ")

    # Erzeuge Liste
    random_numbers = create_sorted_list(start, end)
    print(random_numbers)

    # Suche
    target = get_number("\nSuche: ")
    index = binary_search(target, random_numbers)

    # Ausgabe
    if index == -1:
        print("Nicht gefunden.")
    else:
        print(f"Index: {index}")


if __name__ == '__main__':
    main()
