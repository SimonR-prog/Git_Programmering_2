# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 12.6:

import os
import json

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def importer(): # Function to import the dictionary and return it.
    with open('notepad.json') as f:
        notes_dict = f.read()
        notes_dict = json.loads(notes_dict)
        return notes_dict

def exporter(notes_dict): # Function to export the dictionary again after modifying it.
    with open('notepad.json', 'w') as f:
        f.write(json.dumps(notes_dict))

def changer(choice): # Function to remove, add or change a note.
    notes_dict = importer() # Fetches the dictionary.
    if choice == "remove":
        print("Which note would you like to remove?")
        key = input("> ").capitalize()
        if key in notes_dict: # Check for it's existence
            print(f"{key} - {notes_dict[key]} has been removed.")
            del notes_dict[key]
            exporter(notes_dict)  # Updates the dict after change has been made.
        else:
            print("There is no such note.")
    elif choice == "add":
        print("What title do you want for the new note?")
        key = input("> ")
        if key.capitalize() not in notes_dict: # If key doesn't already exist.
            print("What text do you want to add to the note?")
            value = input("> ")
            notes_dict[key.capitalize()] = value.capitalize() # Caps both key and text.
            exporter(notes_dict)
        else:
            print("That note already exists.")
    elif choice == "change":
        print("Which one would you like to change?")
        key = input("> ").capitalize()
        if key in notes_dict:
            print(f"Current text is; {notes_dict[key]}")
            print("What would you like to change it to?")
            new_value = input("> ").capitalize()
            notes_dict[key] = new_value
            exporter(notes_dict)
        else:
            print("There's no such note.")

def viewer(): # Function to print the value of the key the person chooses.
    notes_dict = importer()
    if len(notes_dict) > 0:
        print("Would you like to view all or a specific note? (All/Spec)")
        choice = input("> ").lower()
        if choice == "all":
            print("-"*20)
            for i in notes_dict:
                print(i + ";\n-" + notes_dict[i])
        elif choice == "spec":
            print("Which note would you like to view?")
            view = input("> ").capitalize()
            if view in notes_dict:
                print("-" * 20)
                print(notes_dict[view])
            else:
                print("There's no such note.")
        else:
            print('You have to type either "all" or "spec".')
    else:
        print("The file is empty.")

def menu(): # Function to print the menu, the list of keys and the instructions.
    notes_dict = importer()
    print("*"*20)
    print("Notes".center(20))
    print("*"*20)
    for i in notes_dict:
        print(i)
    print("*"*20)
    instructions = {"View":"View note", "Add":"Add note","Remove":"Remove note","Change":"Change note text","Exit":"End program"}
    print("Instructions".center(20))
    print("*"*20)
    for i in instructions:
        print(i + " - " + instructions[i])
    print("*"*20)

while True:
    clear_console()
    menu()
    menu_choice = ["view","add","remove","change","show","exit"]
    choice = input("> ").lower()
    if choice in menu_choice:
        if choice == "view":
            viewer()
        elif choice in ["add","remove","change"]:
            changer(choice)
        elif choice == "exit":
            print("Ending program.")
            break
    else:
        print("Must choose from the list of instructions.")
    print("-" * 20)
    enter = input("Press enter to continue.")
