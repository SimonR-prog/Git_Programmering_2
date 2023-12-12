# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 13.3:

import os
import requests
import json


def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def menu(): # Function to make a menu in console. Imports the dictionary and prints keys.
    artist_dict = artists()
    print("*"*30)
    print(">-<> Artist info! <>-<".center(30))
    print("*" * 30)
    print("Artist list;".center(30))
    print("*"*30)
    for i in artist_dict:
        print(i)
    print("*" * 30)
    print("Menu; \n1. Get information on an artist. \n2. Exit.")
    print("*" * 30)

def artists():
    # Function to import the dictionary, extract the
    # necessary information and put it in a dictionary.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
    r = requests.get(url)
    text = json.loads(r.text)
    # Remakes the dictionary everytime it runs which renews the ID's.
    artist_dict = {}
    x = 0
    for i in text['artists']:
        artist_dict[text['artists'][x]['name']] = text['artists'][x]['id']
        x += 1
    return artist_dict

def id_num(): # Function to get the ID number of artist.
    name = input("Which artist? > ").title()
    artist_dict = artists()
    if name in artist_dict:
        id = artist_dict[name]
        information(id)
    else:
        print("That artist is not on the list.")

def information(id): # Function to extract the information and create variables.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + id
    r = requests.get(url)
    artist_info = r.json()

    # Creating variables;
    genre = artist_info['artist']['genres']
    active = artist_info['artist']['years_active']
    members = artist_info['artist']['members']
    name = artist_info['artist']['name']
    printer(genre, active, members, name)

def printer(genre, active, members, name): # Function to print the information depending on len of info.
    print("*"*30)
    if len(genre) == 1:
        print(f"The genres of {name} are {genre[0].capitalize()}.")
    elif len(genre) > 1:
        print(f"The genres of {name} are " + ", ".join(genre[0:-1]) + f" and {genre[-1]}.")
    if len(active) == 1:
        print(f"The active years of {name} are {active[0]}.")
    elif len(active) > 1:
        print(f"The active years of {name} are " + ", ".join(active[0:-1]) + f" and {active[-1]}.")
    if len(members) == 1:
        print(f"The only member of {name} is named {members[0].title()}.")
    elif len(genre) > 1:
        print(f"The names of the members of {name} are " + ", ".join(members[0:-1]) + f" and {members[-1]}.")

while True:
    # Clearing console on start.
    clear_console()
    # Prints out menu with artist names and menu options.
    menu()
    menu_choice = input(" > ")
    if menu_choice == "1":
        id_num()
    elif menu_choice in ["2", "Exit","exit"]:
        print("Ending program.")
        break
    else:
        print("Invalid input.")
    # Enter input for pause.
    print("*"*30)
    enter = input("Press enter to continue.. ")




