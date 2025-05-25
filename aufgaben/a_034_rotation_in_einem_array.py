"""
Verschiebt alle Elemente eines Arrays um eine Position nach rechts, das letzte
Element landet vorne.
"""

def _get_elements():
    elements =[]
    while True:
        element = input("Element: ")
        if element in "xX":
            break
        elements.append(element)
    return elements

print("Elemente eingeben. X zum Beenden.")
elements = _get_elements()
last = elements.pop(-1)
elements.insert(0,last)
print(elements)