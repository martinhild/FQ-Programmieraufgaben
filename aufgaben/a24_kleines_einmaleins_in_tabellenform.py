platz_pro_zahl = 4


for i in range(1,11):
    print(f"{i:{platz_pro_zahl}}", end="")
    for j in range(1,11):
        print(f"{i * j:{platz_pro_zahl}}", end="")
    print()
