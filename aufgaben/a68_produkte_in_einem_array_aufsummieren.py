"""
Lese 5 Preise ein und speichere sie in einem Array. Gib anschließend die Gesamtsumme aus.
"""
from utils.user_inputs import get_float

def _get_prices():
    prices =[get_float(f"Preis: ") for i in range (1,6)] # List Comprehension
    """
    List Comprehensions funktionieren nur mit einem for und einem iterierbaren
    Objekt (zB range, list, str, tuple, set, dict, Generator etc.)
    """
    return prices

print(sum(_get_prices()))

