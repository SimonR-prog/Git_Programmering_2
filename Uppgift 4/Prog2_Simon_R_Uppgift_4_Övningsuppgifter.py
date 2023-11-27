# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf
import os

# 5.1;
# Take an intger input, double it and print. If input != int then print error message.

number = input("Number; > ")
try:
    result = int(number) * 2
    print(result)
except ValueError:
    print("ValueError. Must input a number.")

# 5.2;
# Input for two floats, try excepts for div by 0 and valueerrors.
# Divide the numbers and print the result

number_1 = input("Number 1 > ")
number_2 = input("Number 2 > ")
try:
    result = float(number_1) / float(number_2)
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("ValueError. Must input a number.")

# 5.3;
# Make program with unknown amounts of inputs until user types exit.
# When exit; print amount of numbers added, total sum of the numbers
# and average value of numbers added.

sum = 0
amount = 0
print("Type numbers to add. Type exit to end.")
while True:
    number = input("> ").lower()
    if number == "exit":
        print("Ending.")
        break
    else:
        try:
            sum += int(number)
            amount += 1
        except ValueError:
            print("ValueError. Must input a whole number.")
try:
    print("Amount of numbers added; ", amount)
    print("Sum of the numbers added; ", sum)
    print("Average value of the numbers added; ", sum/amount)
except ZeroDivisionError:
    print("Can't divide by zero.")


# 6.1;
# Input a string, use another input to ask for a letter.
# Count the amount of times the letter is in the string.
# Have to use while loop, no for loop.

string = input("Which string would you like to use? > ")
letter = input("Which letter would you like to count? > ")
string_len = len(string)
i = 0
try:
    check_string = str(string)
    check_letter = str(letter)
    while i < string_len:
        letter_count = check_string.count(check_letter)
        break
except ValueError:
    print("ValueError. Must input string in the inputs.")
print(letter_count)


# 6.2;
# Robber Translate; After every consonant; Add "o" and the same consonant again.

consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
             "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
strings = input("What would you like to make into rövarspråk? > ")
robber = ""
for i in strings:
    if i in consonant:
        robber += i + "o" + i
    else:
        robber += i
print(robber)

# 6.3;
# Make a program that checks if something is a palindrome.
# Need to make the word lower() and then reverse it.

check = input("Which string would oyu like to check if it is a palindrome? > ")
checking = check.lower()
if checking == checking[::-1]:
    print(f"Yes, {check} is a palindrome.")
else:
    print(f"Nah, {check} is not a palindrome.")


# 7.1;
# Create a billboard that the user can change.
#

line_1 = ""
line_2 = ""
line_3 = ""
size = 20
while True:
    # Clear os;
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print("*" * size)
    print("Billboard".center(size))
    print("*" * size)
    print(line_1)
    print(line_2)
    print(line_3)
    print("*"*size)
    print("1. Change one of the lines.\n2.Close program.")
    choice = input("Command; > ")
    if choice == "1":
        choice_which = input("Which on would you like to change? (1,2 or 3) > ")
        new_line = input("Input new string; > ")
        if choice_which == "1":
            line_1 = new_line
        elif choice_which == "2":
            line_2 = new_line
        elif choice_which == "3":
            line_3 = new_line
    elif choice == "2":
        print("Ending program")
        break
    else:
        print("Must choose one of the options.")


















