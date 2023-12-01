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
    If not on list, allow user to add it.
"""

import os

todo = ["Städa", "Handla", "Plugga", "Ge blod"]

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def print_list(): # Function to print the to do list..
    todo.sort()
    list_index = 1
    print("*" * 15)
    print("To do list;".center(15))
    for i in todo:
        # Convert the int to string to concatenate.
        # Adding number before each to use later for removing indexes.
        print(str(list_index) + ". " + i)
        list_index += 1


def remove_todo(): # Function to remove things from to do list with either name of thing or index.
    print("What would you like to remove? \n(You can type the name of the thing or use the number next to it.)")
    choice = input(" Choose; > ").capitalize()
    if choice in todo:
        todo.remove(choice)
        print(f"Removing {choice}")
    else: # If choice not in list, it is either an invalid input or a number.
        try: # Valid input that is a number.
            pop = (int(choice) - 1)
            print(f"Removing {todo[pop]}")
            todo.pop(pop)
        except:
            if choice.isnumeric(): # Invalid input that is a number.
                print(f"There is no number {choice} on the to do list.")
            else: # Invalid input that is a string.
                print(f"{choice} is not on the list.")


def add_todo(): # Function to add things with append if it isn't on the list.
    choice = input("What would you like to add to your to do list? > ")
    if choice in todo:
        print(f"{choice} is already in the list.")
    else:
        print(f"Adding {choice} to the list.")
        todo.append(choice.capitalize())


def check_list():
    check_for = input("Which item are you looking for on your list? > ").capitalize()
    if check_for in todo:
        print(f"Yes, {check_for} is on your to do list.")
    else:
        print(f"{check_for} is not on the to do list.")
        choice = input("Would you like to add it? Y/N > ").lower()
        if choice == "yes" or choice == "y":
            todo.append(check_for.capitalize())
        else:
            print("Alright.")


while True:
    # Running clear console and list printing functions from start. the others on command.
    clear_console()
    print_list()
    print("*"*15)
    choice = input("  Command; \n1. Add a thing to do. \n2. Remove a thing from to do. \n3. Check for item on list. \n4. Close. \nChoose; > ")
    if choice == "1":
        add_todo()
    elif choice == "2":
        remove_todo()
    elif choice == "3":
        check_list()
    elif choice == "4":
        print("Ending program.")
        break
    else:
        print("Invalid input.")
    # Adding this to make sure people have time to read the messages.
    enter = input("Press enter to continue.")

