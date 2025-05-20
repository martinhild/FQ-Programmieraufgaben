
##############################################################
#            Version a (aufwendiger): Vergleichen            #
#              der Primfaktorzerlegungen beider Zahlen       #
##############################################################


def _get_numbers():
    """returns two numbers from user input """
    num1 = int(input("a: "))
    num2 = int(input("b: "))
    return num1, num2

def is_prime(n):
    """ checks if a number is prime """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def _get_primes_of_number(number):
    """
    returns dictionary of primes and exponents
    For example: 90 returns {2: 1, 3: 2, 5: 1}
    """
    primes_of_number = {}
    for i in range(2, number+1): # number+1 in case number itself is a prime
        x = 0
        while True:
            if number % i == 0:
                x +=1
                number //= i
            else:
                if x != 0:
                    primes_of_number[i] = x
                break
    return primes_of_number

def compare_dicts(dict_1, dict_2):
    """
    compares two dicts and return a new dict with common primes and their exponents
    """
    new_dict = {}
    for n in dict_1:
        if n in dict_1 and n in dict_2:
            if dict_1[n] < dict_2[n]:
                new_dict[n] = dict_1[n]
            else:
                new_dict[n] = dict_2[n]
    return new_dict

def _get_ggt(primes_of_a, primes_of_b):
    ggt_dict = compare_dicts(primes_of_a, primes_of_b)
    ggt = 1
    for key, value in ggt_dict.items():
        ggt = ggt * key ** value
    return ggt


def main():
    a, b = _get_numbers()
    primes_of_a = _get_primes_of_number(a)
    primes_of_b = _get_primes_of_number(b)
    ggt = _get_ggt(primes_of_a, primes_of_b)
    kgv = a*b / ggt
    print(f"ggT: {ggt}")
    print(f"kgV: {kgv}")


if __name__=="__main__":
    main()



