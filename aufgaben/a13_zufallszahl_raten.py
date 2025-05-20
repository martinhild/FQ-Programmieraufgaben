import random

MIN = 0
MAX = 100

def _get_user_guess(min_val, max_val):
    while True:
        try:
            user_guess = int(input(f"\nGuess: "))
            if min_val <= user_guess <= max_val:
                return user_guess
            else:
                print(f"Number must be between {min_val} and {max_val}")
        except ValueError:
            print("Must be integer!")

def check_guess(guess, correct):
    if guess==correct:
        print("Correct!")
        return True
    else:
        if guess < correct:
            print("Too low!")
            return False
        else:
            print("Too high!")
            return False


def main():
    random_number = random.randint(MIN, MAX)
    print(f"\nGuess number between {MIN} and {MAX}")

    while True:
        user_guess = _get_user_guess(MIN, MAX)
        if check_guess(user_guess,random_number):
            break


if __name__ == "__main__":
    main()