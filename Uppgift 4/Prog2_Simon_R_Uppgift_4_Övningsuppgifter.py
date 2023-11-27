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













