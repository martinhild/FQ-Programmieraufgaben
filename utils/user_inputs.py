def get_number():
    """ Returns a number from user input. """
    while True:
        try:
            num1 = int(input("Number 1: "))
            return num1
        except ValueError:
            print("must be integer\n")


def get_numbers():
    """ Returns two numbers from user input. """
    while True:
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            return num1, num2
        except ValueError:
            print("must be integer\n")