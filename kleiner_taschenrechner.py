try:
    x = float(input("Zahl 1: "))
    y = float(input("Zahl 1: "))
except ValueError:
    print("Keine Zahl")

zeichen = input("Rechenzeichen: ")

match zeichen:
    case "+":
        ergebnis = x + y
    case "-":
        ergebnis = x - y
    case "*":
        ergebnis = x * y
    case "/":
        if y == 0:
            ergebnis= "kann nicht durch 0 teilen"
        else:
            ergebnis = x / y
    case _:
        ergebnis= "ungültiges Rechenzeichen."

print(ergebnis)
