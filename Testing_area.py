import os
import json

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def menu():
    with open('notepad.json') as f:
        notes_dict = f.read()
        notes_dict = json.loads(notes_dict)
        return notes_dict

def printer(): # to print the keys.
    notes_dict = menu()
    for i in notes_dict:
        print(i)

def printer_2(): # To print the value.
    notes_dict = menu()
    for i in notes_dict:
        print(notes_dict[i][0])


printer()
printer_2()

