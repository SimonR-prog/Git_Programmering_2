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
rad = "-------------------------------" # Spacer for console.
# 8.1;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo[:3]) # Using index. Printing up to 3 but wont print the 3d index.
print(rad)

# or
print(todo[0])
print(todo[1])
print(todo[2])
print(rad)

# or
i = 0
while i < 3:
    print(todo[i])
    i += 1
print(rad)

# 8.2;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
add = input("What would you like to add to the to do? > ").capitalize()
todo.append(add)
print(todo)
print(rad)

# 8.3;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
try:
    pop = int(input("Which index do you want to remove? > "))
    todo.pop(pop)
except:
    print("Must input a whole number for which index you want to remove.")
print(todo)
print(rad)

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
print(rad)

# 8.5;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
add = input("What would you like to add to the list? > ").capitalize()
todo.append(add)
print(f"{add} has been added.")
todo.sort()
print(todo)
print(rad)

# 8.6;
todo = ["Städa","Handla","Plugga","Ge blod"]
print(todo)
check = input("What do you want to check? > ").capitalize()
if check not in todo:
    choice = input(f"{check} is not on the list, would you like to add it? Y/N > ").upper()
    if choice == "Y" or choice == "YES":
        todo.append(check)
        print(f"{check} has been added to the to do.")
    else:
        print("Okey.")
else:
    print(f"{check} is in the to do.")
todo.sort()
print(todo)
