
def loesung_1():
    """ manuell """
    line = input("Zeile: ")
    word = ""
    words = []

    for char in line:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)

    for word in words:
        print(word)

def loesung_2():
    """ pythonic """
    line =  input("Zeile: ")
    words = line.split()
    for word in words:
        print(word)

loesung_1()
loesung_2()