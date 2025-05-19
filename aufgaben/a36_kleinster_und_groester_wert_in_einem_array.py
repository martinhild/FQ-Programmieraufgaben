"""
Speichere eine Liste von Zahlen in einem Array und finde den kleinsten bzw.
größten Wert per Schleife.
"""
from utils.user_inputs import get_float
SIZE = 5

numbers =[]
for n in range(SIZE):
    numbers.append(get_float())

smallest, biggest = numbers[0], numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(f"kleinster Wert: {smallest}")
print(f"größter Wert: {biggest}")