"""writes ascii table for letters in .txt file"""
import os
import re

# Arbeitsverzeichnis
verzeichnis = "../data"

numbers=[]
for i in range(65, 91):
    numbers.append(i)

with open("../data/ascii-Aa-Zz.txt","w") as file:
    for number in numbers:
        space = " " if number < 68 else ""
        line = f"{number}   {chr(number)}       {number+32}{space}   {chr(number+32)}"
        file.write(f"{line}\n")