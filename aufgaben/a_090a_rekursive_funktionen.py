"""
Rekursive Funktionen
a. Implementiere eine rekursive Funktion, die z. B. die Tiefe eines
Verzeichnisbaums ausgibt (oder simpler: die Summe von 1 bis n).

a) Die Summe von 1 bis n
"""
# a) Summe von 1 bis n:

N = 4

def _sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + _sum_recursive(n-1)

print(_sum_recursive(N))



