"""
E-Mail-Validierung
a. Schreibe eine Funktion, die prüft, ob ein String eine gültige
E-Mail-Adresse sein kann.
"""

import re


def check_local(local):
    """
    Prüft den lokalen Teil einer Mail-Adresse.
    Regeln:
    - Erlaubte Zeichen: Buchstaben, Ziffern, Sonderzeichen.
    - Punkte nicht am Anfang, Ende oder hintereinander.
    """
    # Verbotene Muster
    forbidden_patterns = [
        r"\.\.",  # Zwei Punkte in Folge
        r"^\.",   # Beginnt mit Punkt
        r"\.$"   # Endet mit Punkt
    ]

    # Muster für erlaubte Zeichen
    allowed_pattern = r"[a-zA-Z0-9!#$%&'*+/=?^_{|}~`\-\.]+"
    if not re.fullmatch(allowed_pattern, local):
        return False

    # Prüft local auf verbotene Muster
    if check_with_patterns(local, forbidden_patterns):
        return False
    return True


def check_domain(domain):
    """
    Prüft den domain-Teil einer Mail-Adresse.
    Regeln:
    - Erlaubte Zeichen: Buchstaben, Ziffern, Bindestriche, Punkte.
    - Mindestens ein Punkt.
    - bindestriche nicht am Anfang oder Ende eines Segments.
    - Segmente dürfen nicht mit Punkt beginnen oder enden.
    """
    forbidden_patterns = [
        r"^\.",   # Beginnt mit Punkt
        r"\.$",  # Endet mit Punkt
        r"\.\.",  # Zwei Punkte in Folge
        r"^-",   # Beginnt mit Bindestrich
        r"-$",    # Endet mit Bindestrich
        r"--",    # Zwei Bindestriche in Folge
        r"\.-",   # Punkt Bindestrich
        r"-\.",   # Bindestrich Punkt

    ]

    # Muster für erlaubte Zeichen
    pattern = r"[a-zA-Z0-9\-\.]+"
    if not re.fullmatch(pattern, domain):
        return False

    # Mindestens ein Punkt
    if domain.count(".") < 1:
        return False

    # Prüft domain auf verbotene Muster
    if check_with_patterns(domain, forbidden_patterns):
        return False
    return True


def check_mail_address(text):
    """
    Prüft Gültigkeit der Local und Domain Teile einer Mailadresse.
    Übergibt dafür die Teile der Funktion check_local().
    """
    # Nur ein @-Zeichen. Auftelung in Local und Domain
    if text.count("@") != 1:
        return False
    local, domain = text.split("@")
    if not check_local(local) or not check_domain(domain):
        return False
    return True


def check_with_patterns(text, patterns):
    """
    Prüft text gegen eine Liste aus Regex-Mustern.
    Gibt False zurück, wenn text einem Muster entspricht.
    """
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False


def main():
    while True:
        mail_address = input("\nAbbruch mit \"X\"\"\nE-Mail Adresse: ")

        # Beenden mit X
        if mail_address in "xX":
            break

        # Prüfung und Ausgabe:
        if check_mail_address(mail_address):
            print("gültige Mail-Adresse")
        else:
            print("ungültige Mail-Adresse")


if __name__ == "__main__":
    main()
