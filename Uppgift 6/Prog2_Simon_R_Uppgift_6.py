# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 12.6:

""" Defining in no order;
A menu with instructions.
A dictionary with a titel as key and text as value.
User ability to list, show, create, change and remove items from dictionary.
Clear console.
Import and export to a separate file to save between runs.

Want to change it so that the person can type in a number to call for a certain key?

Output;
Clear console.
Print menu with the keys and instructions.


Print the value of the first thing in dict;
print(notes_dict["1"])


"""
import os
import json

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def exporter(notes_dict): # Function to export the dictionary again after modifying it.

    notes_dict["Ny"] = "Nyast"
    # import through other function.

    with open('notepad.json', 'w') as f:
        f.write(json.dumps(notes_dict))

def changer(decide, key): # Function to remove or add a note.
    notes_dict = importer() # Fetches the dictionary.
    if decide == "remove":
        if key.capitalize() in notes_dict: # Check for it's existence
            notes_dict.pop(key.capitalize())
            exporter(notes_dict)
        else:
            print("There is no such note.")
    else:
        if key.capitalize() not in notes_dict: # If key doesn't already exist.
            print("What text do you want to add to the note?")
            value = input("> ")
            notes_dict[key.capitalize()] = value.capitalize() # Caps both key and text.
            exporter(notes_dict)
        else:
            print("That note already exists.")

def importer():
    with open('notepad.json') as f:
        notes_dict = f.read()
        notes_dict = json.loads(notes_dict)
        return notes_dict

def viewer(view): # Function to print the value of the key the person chooses.
    notes_dict = importer()
    if len(notes_dict) > 0:
        if view in notes_dict:
            print(notes_dict[view])
        else:
            print("There's no such note.")
    else:
        print("The file is empty.")
def printer_2(): # To print the value.
    notes_dict = importer()
    for i in notes_dict:
        print(notes_dict[i][0])


def menu():
    notes_dict = importer()
    print("*"*20)
    print("*"*5,"Notes".center(8),"*"*5)
    print("*"*20)
    for i in notes_dict:
        print(i)
    print("*"*20)
    instructions = ["View | View note", "Add | Add note","RM | Remove note","Exit | End program"]
    for i in instructions:
        print(i)

while True:
    clear_console()
    menu()
    choice = input("> ").lower()
    if choice in ["view","add","rm","exit"]:
        if choice == "view":
            print("Which would you like to view?")
            view = input("> ")
            viewer(view)
        elif choice == "add":
            print("What would you like to add?")
            key = input("> ")
            decide = "add"
            changer(decide, key)
        elif choice == "rm":
            print("Which would you like to remove?")
            key = input("> ")
            decide = "remove"
            changer(decide, key)
        elif choice == "exit":
            print("Ending program.")
            break
    enter = input("Press enter to continue.")

"""Want to use the exporter function from adding or removing functions. 
Send a string with either remove or add and then a 
variable to the export function and do an if else.

Change the add turn the thing into a dict variable to later add. 

"""