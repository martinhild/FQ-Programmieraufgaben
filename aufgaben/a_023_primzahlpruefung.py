
# get user input
def _get_user_input():
    while True:
        try:
            user_input = int(input(f"Number: "))
            if user_input >= 0:
                return user_input
            else:
                print("Must be a non-negative integer!\n")
        except ValueError:
            print("Must be integer!\n")


# Primzahl: ganze Zahl, größer als 1, nur durch 1 und sich selbst teilbar
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = _get_user_input()
if is_prime(number):
    print("PRIME!\n")
else:
    print("NO prime...\n")