"""
Analyse von 10 Zufallszahlen
a. Erzeuge 10 Zufallszahlen zwischen 1 und 50. Gib sie aus, ermittle den Durchschnitt und runde ihn auf ganze Zahlen.
"""
import random

zahlen = []
for i in range(10):
    x = random.randint(1,50)
    zahlen.append(x)
    print(x)

total = sum(zahlen)
avg = total / len(zahlen)

print(f"Average: {avg:.0f}")