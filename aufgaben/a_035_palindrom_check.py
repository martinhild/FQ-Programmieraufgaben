"""
Prüfe, ob ein eingegebener String ein Palindrom ist (vorwärts und rückwärts
gleich).
"""

def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False

user_input = input("Eingabe: ")
answer = "Palindrom!" if is_palindrome(user_input) else "Kein Palindrom"
print(answer)