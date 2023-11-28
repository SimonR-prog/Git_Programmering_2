# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf
# 8.2
"""Define;
Assignment wants us to do several things with the same to do list;
1. Print out the first three of the things in the list.
2. Print out the list. Append the list with "Fetch dog..". Print it out again.
3. Allow user to remove a thing of the list by inputting an index.
Print the list before and after to confirm.
Need list.pop(index)
4. Allow user to remove a thing via value input. 
If x in list yadayada.. Use remove(element).
5. Allow user to add something to the list and then sort it. Print before and 
after. string.sort()
6. Through input, user can check if something is in list. If x in list = response
if x not in list = respone + ask if user wants to add it. Print list yadayada..
"""
# 8.1;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo[:3])
# or
print(todo[0])
print(todo[1])
print(todo[2])

# 8.2;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
add = input("What would you like to add to the to do? > ").capitalize()
todo.append(add)
print(todo)

# 8.3;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
try:
    pop = int(input("Which index do you want to remove? > "))
    todo.pop(pop)
except:
    print("Must input a whole number for which index you want to remove.")
print(todo)

# 8.4;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
rem = input("Which one would you like to remove? > ").capitalize()
if rem in todo:
    todo.remove(rem)
    print(f"{rem} has been removed.")
else:
    print(f"{rem} is not in to do.")
print(todo)

# 8.5;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
add = input("What would you like to add to the list? > ").capitalize()
todo.append(add)
print(f"{add} has been added.")
todo.sort()
print(todo)

# 8.6;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
add = input("What to do? > ").capitalize()
if add not in todo:
    choice = input(f"{add} is not on the list, would you like to add it? Y/N > ").upper()
    if choice == "Y" or choice == "YES":
        todo.append(add)
        print(f"{add} has been added to the to do.")
    else:
        print("Okey.")
else:
    print(f"{add} is in the to do.")
todo.sort()
print(todo)




# Creating a program for a to do with while loop for fun;
"""
Clear console everytime. 
Show the list. 
    Print it with a for loop to add numbers to all things for easy removal with index.
Allow person to remove things by index or name of thing.
    When using index, remove 1 from the number they input to get the index.
    Ask them for a y/n before removing.
Allow person to add things to the list.
Allow person to check if something is on the list.
"""
import os
# Starting list;
todo = ["Städa","Handla","Plugga","Ge blod"]
while True:
    # Clear os;
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    for i in todo:
        print(todo[i]," ", i)


















