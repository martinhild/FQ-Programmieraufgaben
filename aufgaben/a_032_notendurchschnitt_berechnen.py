"""
liest Noten für Schulfächer ein und gibt sie zusammen mit der
Durchschnittsnote und Bewertungen wieder aus
"""
from utils import user_inputs

SUBJECTS = ["Deutsch", "Mathe", "Englisch", "Physik", "Erdkunde", "Chemie"]
GRADE_NAMES = {
    1: "sehr gut",
    2: "gut",
    3: "befriedigend",
    4: "ausreichend",
    5: "mangelhaft",
    6: "ungenügend"
}

print("\nGib deine Noten ein.")

grades={}
total = 0
for subject in SUBJECTS:
    print(f"{subject}: ", end="")
    grade = user_inputs.get_number()
    grades[subject] = grade
    total += grade

grades["Durchschnitt"] = round(total/len(grades))

print("\nBewertung:\n")
for grade in grades:
    grade_name = GRADE_NAMES[grades[grade]]
    print(f"{grade}: {grade_name}")

