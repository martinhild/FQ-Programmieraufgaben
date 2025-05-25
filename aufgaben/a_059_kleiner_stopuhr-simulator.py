"""
 Kleiner Stopuhr-Simulator
a. Starte eine Schleife, die jede Sekunde „tick“ ausgibt. Beende sie nach einer
eingegebenen Zahl n (Sekunden).
"""
import time
from utils.user_inputs import get_number

n = get_number("Seconds: ")
for i in range(n):
    print(f"Seconds:  {n-1 - i}  *tick*")
    time.sleep(1)
