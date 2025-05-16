def ergebnis_ausgeben():
    minimum = min(zahlen)
    maximum = max(zahlen)
    durchschnitt = sum(zahlen)/len(zahlen)
    print(f"Zahlen: {zahlen}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Durchschnitt: {durchschnitt}")

zahlen = []
while True:
    print("Gebe Zahlen ein oder x zum Beenden")
    user_input = input("Eingabe: ")
    if user_input == 'x':
        ergebnis_ausgeben()
        break
    try:
        user_input = int(user_input)
        zahlen.append(user_input)
    except ValueError:
        print("keine Zahl")


