"""
84. Statistiken über Arrays
a. Gib die Anzahl, Summe, Mittelwert, Standardabweichung eines Arrays aus.

Standardabweichung ist die Quadratwurzel der Varianz.
Varianz misst die Streuung der Werte um ihren Mittelwert.
Rechenweg:
1. Durchschnitt der Zahlen
2. Für jede Zahl: (Zahl - Durchschnitt)^2
3. Varianz: Durchschnitt dieser Quadrate.
4. Wurzel aus Varianz ziehen.
"""
import random
import math
import statistics

MIN_RANDOM = 1
MAX_RANDOM = 6
LENGTH_LIST = 100

def create_random_list(length):
    """
    Returns a list of random integers from MIN_RANDOM to MAX_RANDOM.
    """
    return [random.randint(MIN_RANDOM,MAX_RANDOM) for _ in range(length)]


def print_stats(numbers):
    """
    Calculates and prints statistics of list of numbers.
    """
    count = len(numbers)
    total = sum(numbers)
    average = statistics.mean(numbers)
    variance = statistics.variance(numbers)
    std_deviation = math.sqrt(variance)

    print(f"\nAnzahl: {count} Zufallszahlen (von {MIN_RANDOM} bis {MAX_RANDOM})")
    print(f"Summe: {total}")
    print(f"Mittelwert: {average:.2f}")
    print(f"Varianz: {variance:.2f}")
    print(f"Standardabweichung: {std_deviation:.2f}")


def main():
    random_numbers = create_random_list(LENGTH_LIST)
    print_stats(random_numbers)


if __name__ == "__main__":
    main()

