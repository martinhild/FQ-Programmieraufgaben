"""
Geburtstagsausgabe
a. Lese das Geburtsjahr einer Person ein und das aktuelle Jahr. Gib anschließend
aus, wie alt die Person ist oder wird
"""
from utils.user_inputs import get_number

born = get_number("Born: ")
now = get_number("Current year: ")

print(f"You are (turning) {now-born} this year.")