"""
my helper functions for user input
"""

def prompt(msg):
    """just print() without line break"""
    print(msg, end="")

def get_number(prompt_text):
    """ Returns a number from user input. """
    while True:
        try:
            return int(input(prompt_text))

        except ValueError:
            print("must be integer\n")

def get_numbers(text1, text2):
    """ Returns two numbers from user input. """
    while True:
        try:
            num1 = int(input(text1))
            num2 = int(input(text2))
            return num1, num2
        except ValueError:
            print("must be integer\n")

def get_float(prompt_text):
    """ Returns a float from user input. """
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print("must be a decimal number\n")

def get_elements():
    """ Returns a list of user inputs. x or X to finish. """
    print("Elemente eingeben. X zum Beenden.")
    elements =[]
    while True:
        element = input("Element: ")
        if element in "xX":
            break
        elements.append(element)
    return elements