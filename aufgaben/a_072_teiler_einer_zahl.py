"""
Teiler einer Zahl
a. Frage nach einer ganzen Zahl und gib alle ihre (positiven) Teiler aus.
"""
from utils.user_inputs import get_number

def list_divisors(number):
    divisors = [i for i in range(1, number+1) if number % i == 0]
    """ List Comprehension: [ausdruck for element in iterable] """
    """ List Comprehension: [ausdruck for element in iterable] if ..."""
    return divisors

n = get_number("Zahl:")
divisors = list_divisors(n)
print(divisors)