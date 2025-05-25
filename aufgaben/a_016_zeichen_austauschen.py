
user_string = input("String: ")

def variante_1(text):
    new = ""
    for sign in text:
        if sign == " ":
            new += "_"
        else:
            new += sign
    return new


def variante_2(text):
    new = text.replace(" ", "_")
    return new

print(variante_1(user_string))
print(variante_2(user_string))