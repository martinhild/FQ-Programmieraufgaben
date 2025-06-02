"""
Benutzerdefinierte Exceptions
a. Schreibe eine eigene Exception-Klasse und löse diese unter bestimmten
Bedingungen aus.
"""

users = {
    "Alfi": "1234",
    "Jenny": "passwort",
    "Karsten": "abc"
}

# Exception 1
class UserNotFoundError(Exception):
    def __init__(self):
        super().__init__("Benutzer existiert nicht.")

# Exception 2
class PasswordIncorrectError(Exception):
    def __init__(self):
        super().__init__("Password ist falsch.")

# Anwendung der Exceptions
def login(user_name, password):
    if user_name not in users:
        raise UserNotFoundError()
    if users[user_name] != password:
        raise PasswordIncorrectError()
    return f"Willkommen {user_name}"


def main():
    user = input("Benutzername: ")
    pw = input("Passwort: ")
    try:
        answer = login(user, pw)
        print(answer)
    except UserNotFoundError as e:
        print("Fehler: ", e)
    except PasswordIncorrectError as e:
        print("Fehler: ", e)

main()

