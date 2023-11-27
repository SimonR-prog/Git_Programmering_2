# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

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


# 6.2;
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


# 6.3;
# 



















