"""
Kontaktverwaltung
Erstelle ein kleines Programm, das Kontakte (Name, Telefonnummer) in einer
Liste abspeichert und durchsuchen lässt
"""

from classes.contact_management import Person, Contacts

# Telefonbuch in dem Kontakte gespeichert werden.
PHONEBOOK = Contacts()


def new_contact():
    """
    Fragt nach Name und Telefonnummer und fügt einen
    neuen Kontakt zum Telefonbuch hinzu.
    """
    name = input("Wen hinzufügen: ")
    number = input("Telefonnummer: ")
    PHONEBOOK.add_contact(name, number)
    print(f"Hinzugefügt: {name} - {number}\n")

def search_contact():
    """
    Fragt nach Name und Telefonnummer und listet passende Kontakte auf.
    """
    name = input("Wen suchen: ")
    print(f"Suchergebnisse für {name}:")
    print("")
    print(PHONEBOOK.search_by_name(name))
    print("")

def delete_contact():
    """
    Fragt nach einem Namen und entfernt den  Kontakt nach Bestätigung.
    """
    name = input("Wen löschen:")
    if PHONEBOOK.remove_contact(name):
        print(f"{name} wurde gelöscht.\n")
    else:
        print(f"{name} nicht gefunden.\n")

def print_phonebook():
    """
    Zeigt alle Kontakte im Telefonbuch an.
    """
    print("--------------------------------------------")
    print(PHONEBOOK)
    print("--------------------------------------------")


def print_menu():
    """
    Zeigt das Hauptmenü mit Optionen an.
    """
    print("--------------------------------------------")
    print("Eingabe: 1 um die Kontakte anzuzeigen.")
    print("Eingabe: 2 um einen Kontakt hinzuzufügen.")
    print("Eingabe: 3 um einen Kontakt zu suchen.")
    print("Eingabe: 4 um einen Kontakt zu löschen ")
    print("Eingabe: x um zu beenden. ")
    print("--------------------------------------------")




def main():
    """
    Steuert die Benutzereingabe und ruft Funktionen auf.
    """

    PHONEBOOK.add_contact("Joachim Schiller", "01472 548545")
    PHONEBOOK.add_contact("Beathe Kramp", "01431 245315")
    PHONEBOOK.add_contact("Rudi Knaller", "02433 12251")

    while True:
        print_menu()
        user_input = input("Eingabe: ")
        print("")

        match user_input:
            case "1":
                print(PHONEBOOK)
            case "2":
                new_contact()
            case "3":
                search_contact()
            case "4":
                delete_contact()
            case "x":
                break


if __name__ == "__main__":
    main()









