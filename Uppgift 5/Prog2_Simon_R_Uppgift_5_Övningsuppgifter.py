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



def pull():

    

cars = ["Mercedes","Volvo","Toyota"]
while True:
    # Clearing console and printing list in beginning.
    clear_console()
    printing()
    # Taking input from user;
    command = input("push | Push element to stack. \npull | Pull element from stack \nexit | Exit program.").lower()
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



