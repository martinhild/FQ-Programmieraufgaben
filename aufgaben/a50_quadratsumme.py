"""
50. Quadratsumme
a. Lese eine ganze Zahl n ein. Berechne die Summe der Quadrate von 1 bis n (1² + 2²
+ … + n²).

"""
from utils.user_inputs import get_number

print("Number: ",end="")
n = get_number()
numbers = []
for i in range(1, n+1):
    square = i**2
    numbers.append(square)
sum_squares = sum(numbers)
print(f"Sum of squares: {sum_squares}")