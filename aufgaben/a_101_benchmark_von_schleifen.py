"""
Benchmark von Schleifen
a. Vergleiche die Ausführungszeit verschiedener Schleifentypen oder
unterschiedlicher Algorithmen (z. B. for-Schleife vs. while-Schleife).
"""
import time

def compare_while_vs_for(iterations):

    # While
    begin = time.time()
    i = 0
    while True:
        i += 1
        if i == iterations:
            break
    end = time.time()
    print(f"While-Loop Time: {end - begin}")

    # For
    begin = time.time()
    for i in range(iterations):
        pass
    end = time.time()
    print(f"For-Loop Time: {end - begin}")

compare_while_vs_for(100000000)