"""Assignement;
Design and implement a todo list with basic functionality.

Create a while loop;
Implement a menu so that people can use the functions to;
1. Show the to do list.
2. Add a thing onto the list.
3. Remove a thing from the list.
4. Close the program. """


import os

def create_list():
    """Function to create an empty list."""
    todo_list = []
    return todo_list

def add_thing(list):
    """Function to take input from user and add it to the todo list."""
    add = input("Which thing would you like to add? \nTo Do; > ").capitalize()
    if add not in list:
        list.append(add)
        return list
    else:
        print("You already have that on your to do list.")

def printer(list):
    """Function to print out all the information from the todo list into the console."""
    if len(list) > 0:
        for i in sorted(list):
            print("- " + i)
    else:
        print("There is nothing in the to do list.")

def remove_thing(list):
    """Function to take input of which thing to remove from the todo list."""
    if len(list) > 0:
        remove_item = input("Which would you like to remove? > ").capitalize()
        if remove_item in list:
            print(f"Removing; {remove_item}.")
            list.remove(remove_item)
        else:
            print(f"{remove_item} is not in list.")
    else:
        print("There is nothing in the to do list.")

def clear_console():
    """Function to clear the console."""
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


# Creating the list outside the loop otherwise it will create a new empty list every time it loops.
todo_list = create_list()
while True:
    # Clearing console to make it easier to read console.
    clear_console()
    menu_size = 32
    print("-----Menu-----".center(menu_size))
    print("1. Show the to do list. \n2. Add thing to do. \n3. Remove thing from to do list. \n4. Close the program.")
    print("-" * menu_size)
    try:
        choice = int(input("Choice > "))
        if choice in range(5):
            if choice == 1:
                printer(todo_list)
            elif choice == 2:
                add_thing(todo_list)
            elif choice == 3:
                remove_thing(todo_list)
            else:
                print("Shutting down.")
                break
        else:
            print("Invalid input. Choose a number on the list.")
    except:
        print("Invalid input. Choose a number on the list.")
    enter = input("Press enter to continue..")