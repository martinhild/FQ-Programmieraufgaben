"""
Größter Wert in einer Liste
a. Lese n Zahlen ein (n vom Nutzer bestimmt) und finde den größten Wert heraus.
"""
from utils.user_inputs import get_number, get_float

n = get_number("Wie viele Zahlen?: ")
numbers = {}
for i in range(1, n + 1):
    number = get_float(f"Nummer {i}: ")
    numbers[i] = number

max_value = (max(numbers.values()))

"""???"""
key_of_max_value = next(k for k, v in numbers.items() if v == max_value)
"""???"""

print(f"Größter Wert ist die Nummer {key_of_max_value}: {max_value}")

