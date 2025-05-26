"""
Kontaktverwaltung
Erstelle ein kleines Programm, das Kontakte (Name, Telefonnummer) in einer
Liste abspeichert und durchsuchen lässt
"""

contacts = []

class Kontakt:
    def __init__(self, name: str = "", phone_number: str = ""):
            self.name = name
            self.phone_number = phone_number

    def add_contact(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

