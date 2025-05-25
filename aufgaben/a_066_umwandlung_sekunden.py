"""
Umwandlung Sekunden → HH:MM:SS
a. Lese eine Anzahl Sekunden ein (z. B. 3675) und rechne sie in das Format Stunden:Minuten:Sekunden um (z. B. 1:1:15).
"""
from utils.user_inputs import get_float

def calc(sec):
    min = sec // 60
    sec = sec % 60
    h = min // 60
    min = min  % 60
    return h,min,sec

def main():
    seconds = get_float("Sekunden: ")
    h,min,sec = calc(seconds)
    print(f"{h}:{min}:{seconds}")

if __name__=="__main__":
    main()