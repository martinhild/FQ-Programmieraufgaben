
def _get_number(n):
    while True:
        try:
            user_input = int(input(f"Number {n}: "))
            return user_input
        except ValueError:
            print("Must be integer!")

x = _get_number(1)
y = _get_number(2)
z = _get_number(3)

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print(x,y,z)