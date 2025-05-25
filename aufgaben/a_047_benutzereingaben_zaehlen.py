"""
7. Benutzereingaben zählen
a. Lese fortlaufend ganze Zahlen ein, bis „0“ eingegeben wird. Gib dann aus, wie
viele Zahlen insgesamt eingegeben wurden (0 nicht mitzählen)
"""


n = 0
while True:
    try:
        num1 = int(input("Input: "))
        if num1 == 0:
            print(n)
            break
        else:
            n +=1
    except ValueError:
        print("must be integer\n")