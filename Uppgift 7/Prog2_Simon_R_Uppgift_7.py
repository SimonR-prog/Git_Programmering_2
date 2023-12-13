# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 13.3:

import os
import requests

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def menu(): # Function to make a menu in console and show options for user to pick from.
    artist_dict = artists()
    print("*"*30)
    print(">-<> Artist information! <>-<".center(30))
    print("*"*30)
    for i in artist_dict['artists']:
        print(i['name'])
    print("*" * 30)
    print("Instructions;".center(30))
    print(" Type the name of an artist. \n Or type exit to end program.")
    print("*" * 30)

def artists(): # Function to get the artists and the ids.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
    r = requests.get(url)
    artist_dict = r.json()
    return artist_dict

def id_num(name): # Function to get the ID number of artist.
    id = ""
    artist_dict = artists()
    for i in artist_dict['artists']:
        if name == i['name']:
            id = i['id']
            information(id)
    if id == "":
        print("There is no such artist in the list.")

def information(id): # Function to extract the information and create variables.
    url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + id
    r = requests.get(url)
    artist_info = r.json()
    # Creating variables;
    genre = artist_info['artist']['genres']
    active = artist_info['artist']['years_active']
    members = artist_info['artist']['members']
    name = artist_info['artist']['name']
    # Sends the information in lists to printer function.
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
    name = input("Which artist? > ").title()
    if name != "Exit":
        id_num(name)
    elif name == "Exit":
        print("Ending program.")
        break
    # Enter input for pause.
    print("*"*30)
    enter = input("Press enter to continue.. ")


