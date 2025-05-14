n = int(input("Ganzzahl n: "))

def sum_1_to_n(n):
    if n==1:
        return 1
    else:
        return n + sum_1_to_n(n-1)

print (sum_1_to_n(n))