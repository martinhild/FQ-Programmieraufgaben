"""
Fibonacci-Folge
a. Berechne die Fibonacci-Folge bis zu einer bestimmten Zahl n und gib die Folge
aus.
"""

N = 15  # Set length of sequence


# Version 1 (iterativ):
def fib_iterative(length):
    """
    Berechnet die Fibonacci-Folge iterativ.
    """
    sequence = [0, 1]
    for i in range(2, length):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


# Version 2 (rekursiv):
def fib_recursive(length):  # Erzeugt die Folge
    """
    Berechnet die Fibonacci-Folge rekursiv.
    """

    def fib(n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        return fib(n - 1) + fib(n - 2)

    return [fib(i) for i in range(length)]


def main():
    version_1 = fib_iterative(N)
    version_2 = fib_recursive(N)
    print(f"\nIterativ: {version_1}")
    print(f"Rekursiv: {version_2}")


if __name__ == "__main__":
    main()