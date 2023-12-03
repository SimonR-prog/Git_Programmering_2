# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf
# 9.1;

# 1:
sum = 0
for i in range(1000000):
    sum += i
print(sum)

# 2:
sum = 0
for i in range(1,500,2):
    sum += i
print(sum)

# 9.2;

registered =["Anna","Eva","Erik","Lars","Karl"]
cancelled =["Anna","Erik","Karl"]
for i in cancelled:
    registered.remove(i)
print(registered)

# 9.3;

first_name = ["Maria","Erik","Karl"]
last_name = ["Svensson","Karlsson","Andersson"]
num = 0
for i in first_name:
    print(i + " " + last_name[num])
    num += 1

# 9.4;

todo = ["Städa","Handla","Plugga","Ge blod"]

print(".:To do:.".center(8))
print("*" * 8)
for i in todo:
    print("-" + i)

# 9.5;
import os
cars = ["Mercedes","Volvo","Toyota"]

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def printing(): # Function to print list.
    print(".:Stackmaster:.".center(14))
    print("*" * 14)
    for i in cars:
        print("-" + i)
    print(".:MENU:.".center(14))

def push():
    add = input("What would you like to push? > ").capitalize()
    if add not in cars:
        print(f"Adding {add}")
        cars.append(add)
    else:
        print(f"{add} is already on the list.")

def pull():
    pop = cars.pop()
    print(f"Removing {pop}")

while True:
    # Clearing console and printing list in beginning.
    clear_console()
    printing()
    # Taking input from user;
    command = input("push | Push element to stack. \npull | Pull element from stack \nexit | Exit program. \nCommand > ").lower()
    if command in ["push","pull","exit"]:
        if command == "push":
            push()
        elif command == "pull":
            pull()
        else: # Only exit left.
            break
    else:
        print("Invalid command. Must choose from the list.")
    enter = input("Press enter to continue.")

# 10.1:
# Create a roadsign with a text part that can be changed.
# Have a string inside a txtfile that can be changed.
# Import it from the txtfile to a variable and then print the var with the rest of the sign.

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def importer(): # Function to read the file and extract the variabel value to later print.
    with open('sign.txt') as f:
        name = f.read()
    roadsign(name)

def roadsign(name):
    print("|","-" * 20,"|")
    print("|","Welcome to", name,"|")
    print("|","-" * 20,"|")
    print("C | Change sign. \nE | Exit program.")

def changer():
    new_name = input("What would you like to change it to? > ")
    with open('sign.txt', 'w') as f:
        f.write(new_name)

while True:
    clear_console()
    # Calling function to print roadsign.
    importer()
    command = input("> ").upper()
    if command in ["C", "CHANGE"]:
        changer()
    elif command in ["E","EXIT"]:
        print("Exiting program.")
        break
    else:
        print("Invalid command.")
    enter = input("Press enter to continue.")


# 10.2:

with open('Uppgift 5/numbers.csv') as f:
    number_list = f.read()
    for i in range(10):
        print(i, ";", number_list.count(str(i)))


# 10.3:

def clear_console(): # Function to clear the console.
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def menu(): # Function to print the menu with options.
    print("People database.")
    print("-"*20)
    print("get_id - Get Person by ID")
    print("scan_f - List people by FORENAME")
    print("scan_s - List people by SURNAME")
    print("exit - Exit program")
    print("-"*20)

def person_id():
    person_id = input("ID = ")
    with open('Uppgift 5/database.csv') as f:
        lines = f.readlines()
        try:
            person = lines[int(person_id)+1]
            person_info = person.split(",")
            print("ID;", person_info[0])
            print("Forename;", person_info[1])
            print("Surname;", person_info[2])
            print("Gender;", person_info[3])
            print("Year;", person_info[4])
        except ValueError:
            print("ValueError. Must input a whole number.")

def search(): # Function to search for a name and then print all with that name.
    search_name = input("Name = ").capitalize()
    with open('Uppgift 5/database.csv') as f:
        lines = f.readlines()
        if search_name.isalpha(): # Will probably not work with names that have "-" in them.. Maybe need to change it to is not isnumeric..
            for i in lines:
                if search_name in i:
                    remove_newline = i.replace("\n","")
                    name = remove_newline.replace(",",", ")
                    print(name)
        else:
            print("Must input a name.")

while True:
    clear_console()
    menu()
    command = input("> ")
    print("-"*20)
    if command in ["get_id", "scan_f", "scan_s", "exit"]:
        if command == "get_id":
            person_id()
        elif command in ["scan_f", "scan_s"]:
            search()
        else:
            print("Ending program.")
            break
    else:
        print("Invalid command.")
    print("-"*20)
    enter = input("Press enter to continue. ")


import json
# 11.1:

random_stuff = [1337, 13.37, 'Ååh Yää!']
random_stuff = json.dumps(random_stuff)
print(random_stuff)

# 11.2:

my_chars = '["abc","\u00e5\u00e4\u00f6", "123"]'
my_chars = json.loads(my_chars)
print(my_chars)

































