"""
Mitternachtsformel (Quadratische Gleichung)
a. Lese die Koeffizienten a, b, c ein (ax² + bx + c = 0).
b. Berechne die Diskriminante D = b² - 4ac.
c. Gib die Anzahl der Lösungen aus (keine, eine oder zwei) – genaue Lösungen
kannst du optional ebenfalls ausgeben.
x = (-b +- sqrt(b²-4ac))/2a

"""
import math
from utils.user_inputs import get_float


def _get_abc():
    print("a: ", end="")
    a = get_float()
    print("b: ", end="")
    b = get_float()
    print("c: ", end="")
    c = get_float()
    return a, b, c

def calc_x1(a,b,c):
    try:
        x = ((-1 * b) + math.sqrt(b**2-4*a*c))/ (2 * a)
        return x
    except ValueError:
        return None

def calc_x2(a,b,c):
    try:
        x = ((-1 * b) - math.sqrt(b**2-4*a*c))/ (2 * a)
        return x
    except ValueError:
        return None

def main():
    a, b, c = _get_abc()
    x1 = calc_x1(a,b,c)
    x2 = calc_x2(a,b,c)
    print(f"x1={x1},\nx2={x2}")
    print(calc_x1(3, -14, 8))
if __name__=="__main__":
    main()