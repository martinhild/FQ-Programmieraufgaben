
def _get_user_input():
    while True:
        try:
            user_input = int(input(f"Number: "))
            if user_input >= 0:
                return user_input
            else:
                print("Must be a non-negative integer!")
        except ValueError:
            print("Must be integer!")

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

number = _get_user_input()
f = factorial(number)
print(f)

