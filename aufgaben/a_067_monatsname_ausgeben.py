"""
Monatsname ausgeben
a. Frage nach einer Zahl 1–12 und gib den zugehörigen Monatsnamen aus (1→Januar, 2→Februar, …).
"""

MONTHS = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember"
}

def _get_number(prompt_text):
    while True:
        try:
            x = int(input(prompt_text))
            if 1 <= x <= 12:
                return x
            else:
                print("Zahl ist nicht von 1 bis 12")
        except ValueError:
            print("must be integer\n")

def main():
    n = _get_number("Zahl von 1 bis 12: ")
    print(MONTHS[n])

if __name__=="__main__":
    main()