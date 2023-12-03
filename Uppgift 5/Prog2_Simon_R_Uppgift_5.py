# 11.3:

import json
import os

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def counter(): # Function to sum up everything in the file and send sum and list to menu.
    with open('memorizer.json') as f:
        int_list = f.read()
        int_list = json.loads(int_list)
    sum = 0
    for i in int_list:
        sum += int(i)
    menu(int_list,sum)

def menu(int_list,sum): # Function to print the menu, previous numbers, the sum and the instructions.
    print("*"*20)
    print("Intmemorizer;".center(20))
    print("*"*20)
    for i in int_list:
        print("*",i)
    print("-"*20)
    print("Summa;", sum)
    print("-" * 20)
    print("Input whole numbers.")
    print('Typing "0" will close program.')
    print("-"*20)

def export(number): # Function to add the new number to list and then write it to the file.
    with open('memorizer.json') as f:
        int_list = f.read()
        int_list = json.loads(int_list)
    if number not in int_list:
        int_list.append(number)
        with open('memorizer.json', 'w') as f:
            f.write(json.dumps(int_list))

while True:
    # Clearing console every time loop starts;
    clear_console()
    # Starts the counter function;
    counter()
    # Try/except to catch ValueErrors.
    try:
        number = int(input("> "))
        if number != 0: # If number isn't a 0 it gets sent on to export function.
            export(number)
        else:
            print("Closing.")
            break
    except ValueError:
        print("ValueError. Must type a number.")
        enter = input("Press enter to continue.")
