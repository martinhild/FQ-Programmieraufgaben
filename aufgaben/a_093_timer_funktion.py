"""
Timer-Funktion
a. Implementiere eine Stoppuhr oder einen Countdown-Timer, der nach Ablauf eine
Nachricht anzeigt.
"""
import time


def countdown(seconds):
    for sec in range(seconds, 0, -1):
        print(sec)
        time.sleep(1)


print("Start Countdown.")
countdown(5)
print("Time is over.")