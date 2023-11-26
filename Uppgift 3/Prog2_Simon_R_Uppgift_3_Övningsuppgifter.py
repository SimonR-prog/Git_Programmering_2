#3.1
try:
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
except:
    print("Invalid input.")
#3.2

"""Assignment;
Take name input.
Age input

Output;
How many hours of sleep needed, depending on age. """

#Using dict with age for key and hours of sleep as value:
sleep = {1:14, 2:13, 3:12, 4:11.5, 5 and 6:11,7:10.5, 8 and 9 and 10:10, 11:9.5, 12 and 13 and 14 and 15:9, 16:8.5}
try:
    name = str(input("What is your name? > "))
    age = int(input("What is your age? > "))
    if age in sleep: # Checking if age is in the dict, prints value of key.
        print(f"Hello, {name}. You need {sleep[age]} hours of sleep.")
    elif age in range(17,100): # Using range for the last bit. Could use (elif age >= 17 aswell..)
        print(f"Hello, {name}. You need 8 hours of sleep.")
    else:
        print("You sleep well when dead or not born..")
except:
    print("Invalid input.")

#3.3;












