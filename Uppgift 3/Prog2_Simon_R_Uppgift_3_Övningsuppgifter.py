# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf assignments:


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
sleep = {1:14, 2:13, 3:12, 4:11.5, 5 and 6:11, 7:10.5, 8 and 9 and 10:10, 11:9.5, 12 and 13 and 14 and 15:9, 16:8.5}
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

import random
dice_width = 11
while True:
    dice = random.randint(1, 6)
    roll = input('Type "roll" to roll the dice and "end" to end. > ').lower()
    if roll == "roll":
        print(f"You rolled a {dice}!")
        if dice == 1:
            print(dice_width * "-")
            print("|", " " * 7,"|")
            print("|"," "*2,"X"," "*2,"|")
            print("|", " " * 7, "|")
            print(dice_width * "-")
        elif dice == 2:
            print(dice_width * "-")
            print("|", "X", " " * 5, "|")
            print("|", " " * 7, "|")
            print("|", " " * 5, "X", "|")
            print(dice_width * "-")
        elif dice == 3:
            print(dice_width * "-")
            print("|", "X", " " * 5, "|")
            print("|"," "*2,"X"," "*2,"|")
            print("|", " " * 5, "X", "|")
            print(dice_width * "-")
        elif dice == 4:
            print(dice_width * "-")
            print("|","X", " " * 3, "X", "|")
            print("|", " " * 7,"|")
            print("|","X", " " * 3, "X", "|")
            print(dice_width * "-")
        elif dice == 5:
            print(dice_width * "-")
            print("|", "X", " " * 3, "X", "|")
            print("|", " " * 2, "X", " " * 2, "|")
            print("|", "X", " " * 3, "X", "|")
            print(dice_width * "-")
        else:
            print(dice_width * "-")
            print("|", "X", " " * 3, "X", "|")
            print("|", "X", " " * 3, "X", "|")
            print("|", "X", " " * 3, "X", "|")
            print(dice_width * "-")
    elif roll == "end":
        break


#3.4;

norden = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
great_britain = ["England", "Irland","Scotland","Wales"]

country = input("Write the name of a country. > ").capitalize()
if country in norden:
    print(f"{country} is a part of norden.")
elif country in great_britain:
    print(f"{country} is a part of great britain.")
else:
    print(f"{country} is not part of either norden or storbritanien")


#4.1;

"""Assignment;
Take input one number at a time.
If number is not negative then add it into a list.
If negative, end program. Don't add the negative number.

Output:
print lowest number in the list.
print highest number in the list.
print out the sum of all the numbers.
print out average value, sum of list / len of list.
"""

numbers = []
sum = 0
while True:
    try:
        number = input("Type a number; > ")
        if float(number) > 0:
            numbers.append(float(number))
            sum += float(number)
        else:
            # Sorting the list of numbers and then printing the first and
            # last, and sum of list divided by length of the list.
            numbers.sort()
            print(f"Lowest number is; {numbers[0]}")
            print(f"Highest number is; {numbers[-1]}")
            print(f"The sum of all numbers is; {sum}")
            print(f"The average value of the numbers is; {(sum/len(numbers))}")
            break
    except:
        print("Must input a number.")


#4.2

"""Assignment;
Input number.
Multiply it three times while printing.
Ask if continue or not.

Output;
Print print the multiplikation.
"""

multi = 1
choice = int(input("What number; > "))
while True:
    print(choice * multi)
    multi += 1
    print(choice * multi)
    multi += 1
    print(choice * multi)
    multi += 1
    cont = input("Continue? Y/N > ").upper()
    if cont == "Y":
        continue
    else:
        print("Closing.")
        break
