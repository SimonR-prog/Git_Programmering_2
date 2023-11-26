#3.1

x = int(input("Num.1 > "))
y = int(input("Num.2 > "))
z = int(input("Num.3 > "))

if x > y and x > z:
    print(f"{x} is greatest.")
elif y > x and y > z:
    print(f"{y} is greatest.")
else:
    print(f"{z} is greatest.")

if x < y and x < z:
    print(f"{x} is smallest.")
elif y < x and y < z:
    print(f"{y} is smallest.")
else:
    print(f"{z} is smallest.")


#3.2

