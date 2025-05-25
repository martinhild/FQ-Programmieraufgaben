"""
Zufallszahlensortierung
Erzeuge ein Array mit Zufallszahlen und sortiere es mit einem selbst
implementierten Sortieralgorithmus (z. B. Bubble Sort).
"""

import random

SIZE = 10


def bubble_sort(numbers):
    """Sortiert Liste aus Zahlen mit dem Bubble-Sort-Algorithmus."""
    while True:
        did_swap = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                did_swap = True
        if not did_swap:
            break
    return numbers


def main():
    """
    Liste aus Zufallszahlen von 0 bis 9 wird erstellt und sortiert.
    """
    random_numbers = [random.randint(0, 9) for _ in range(SIZE)]
    print(random_numbers)
    bubble_sort(random_numbers)
    print(random_numbers)


if __name__ == "__main__":
    main()
