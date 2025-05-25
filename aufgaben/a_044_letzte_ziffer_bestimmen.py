"""

a. Lese eine beliebige ganze Zahl (positiv oder negativ) ein und gib die letzte Ziffer
dieser Zahl aus.
b. Beispiel: -1234 → letzte Ziffer: 4.
"""
number = input("Zahl:")
numbers = list(number)
index = int(len(numbers))-1
print(numbers[index])
