"""
Gerade Zahlen in Intervall
a. Lese zwei ganze Zahlen Start und Ende ein. Gib alle geraden Zahlen in diesem
Intervall aus
"""
from utils.user_inputs import get_numbers

start, ende = get_numbers("Start: ","Ende: ")

for i in range(start,ende+1):
    print(i)
