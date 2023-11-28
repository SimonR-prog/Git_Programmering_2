# Creating a program for a to do with while loop for fun;
"""
Clear console everytime it runs.
Show the list.
    Print it with a for loop to add numbers to all things for easy removal with index.
Allow person to remove things by index or name of thing.
    When using index, remove 1 from the number they input to get the index.
    Ask them for a y/n before removing.
Allow person to add things to the list.
Allow person to check if something is on the list.
"""

import os

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def print_list(): # Function to print the to do list..
    list_index = 1
    print("*" * 15)
    print("To do list;".center(15))
    for i in todo:

        # Convert the int to string to concatenate.
        # Adding number before each to use later for removing indexes.

        print(str(list_index) + ". " + i)
        list_index += 1


def remove_todo():
    choice = input("What would you like to remove? \n(Can type the thing or use the number next to it.) \n Choose; > ").lower()

def add_todo():
    choice = input("What would you like to add to your to do list? > ")
    # Need to check so that the string is not a number or whatever..
    if choice in todo:
        print(f"{choice} is already in the list.")

while True:
    # Starting list;
    todo = ["Städa", "Handla", "Plugga", "Ge blod"]
    clear_console()
    print_list()
    print("*"*15)
    choice = input("  Command; \n1. Add thing to do. \n2. Remove a thing from to do. \n4.Close. \nChoose; > ")
    if choice == "1":
        add_todo()
    elif choice == "2":
        remove_todo()
    elif choice == "3":
        continue
    elif choice == "4":
        break
    else:
        print("Invalid input.")















