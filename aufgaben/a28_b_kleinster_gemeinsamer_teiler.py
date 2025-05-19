##############################################################
#        Version b (simpler): Euklidischer Algorithmus:      #
##############################################################

def get_numbers():
    """ Returns two numbers from user input. """
    while True:
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
            return num1, num2
        except ValueError:
            print("must be integer\n")

def get_ggt(a,b):
    """ Returns greatest common divisor using the Euclidean Algorithm. """
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = get_numbers()
    ggt = get_ggt(a, b)
    kgv = a * b // ggt
    print(f"ggT: {ggt}")
    print(f"kgV: {kgv}")


if __name__== "__main__":
    main()