"""Korvkollen;
Defining what we need;
-Need to establish how many of each sausage we need.
-Need to calculate how many packages of each sausage.
-Need to calculate how much the total price is.

Output we want;
-How many packages of each sausage we need to buy.

Normal = 8 per pkg
Vegan = 4 per pkg.

-How many drinks we need 
1 per kid.

-Total of the price.

Price per pkg:
Normal = 20.95 per pkg
Vegan = 34.95 per pkg
Dryck = 13.95 per pkg

"""

import math
#{"type of sausage": amount of kids / amount of sausages.}
saus = {"normal": [0,0], "vegan": [0,0]}


def normal_saus(): #Function to take the input of the normal sausages.
    try: #Try except to catch someone not inputting an intger.
        normal_2 = int(input("How many kids want to eat 2 normal sausages? > "))
        normal_3 = int(input("How many kids want to eat 3 normal sausages? > "))
        amount_saus = (normal_3*3) + (normal_2*2)
        amount_kids = normal_2 + normal_3
        saus["normal"][0] += amount_kids
        saus["normal"][1] += amount_saus
        print(f'Normal sausage total; {saus["normal"][1]}.')
    except ValueError:
        print("Must input a whole number.")

        
def vegan_saus(): #Function to take the input of the vegan sausages.
    try: #Try except to catch someone not inputting an intger.
        vegan_2 = int(input("How many kids want to eat 2 vegan sausages? > "))
        vegan_3 = int(input("How many kids want to eat 3 vegan sausages? > "))
        amount_vegan = (vegan_3*3) + (vegan_2*2)
        amount_kids = vegan_2 + vegan_3
        saus["vegan"][0] += amount_kids 
        saus["vegan"][1] += amount_vegan
        print(f'Vegan sausage total; {saus["vegan"][1]}.')
    except ValueError:
        print("Must input a whole number.")


def calc(): #Function to do all the calculations and print out the information.

#Prices for the pkgs.
    normal_pkg = 20.95
    vegan_pkg = 34.95
    soda_cost = 13.95
    
#Calculating the amount of kids to find out how many sodas and the price of the sodas.
    kids_total = saus["normal"][0] + saus["vegan"][0]
    soda_price = kids_total * soda_cost

#Calc for amount of pkgs of normal and vegan sausages and then calc for price.   
    normal_packages = math.ceil(saus["normal"][1]/8)
    normal_price = normal_packages * normal_pkg
    vegan_packages = math.ceil(saus["vegan"][1]/4)
    vegan_price = vegan_packages * vegan_pkg
    
    total = soda_price + normal_price + vegan_price

    if kids_total > 0:
        if kids_total == 1:
            print(f'\nNeed to buy {kids_total} soda.')
        else:
            print(f'\nNeed to buy {kids_total} sodas.')
        if saus["normal"][0] >= 1: 
            if normal_packages == 1: 
                print(f'{saus["normal"][0]} kid wants normal sausages. Need {normal_packages} package of normal sausages.') 
            else:
                print(f'{saus["normal"][0]} kids want normal sausages. Need {normal_packages} packages of normal sausages.')
        else:
            print("No normal sausages needed.")
        if saus["vegan"][0] >= 1:
            if vegan_packages == 1:
                print(f'{saus["vegan"][0]} kid wants vegan sausages. \nNeed {vegan_packages} package of vegan sausages.')
            elif vegan_packages > 1:
                print(f'{saus["vegan"][0]} kids want vegan sausages. \nNeed {vegan_packages} packages of vegan sausages.')
        else:
            print("No vegan sausages needed.")
        print(f"The total cost is; {total}")
    else:
        print("\nYou haven't added any kids into the system yet.")


while True: #Simple while loop taking simple input for different actions.
    choice = input("\nWelcome. \n1. Add normal sausages. \n2. Add vegan sausages. \n3. Calculate. \n4. End program. \n> ")
    if choice == "1":
        normal_saus()
    elif choice == "2":
        vegan_saus()
    elif choice == "3":
        calc()
    elif choice == "4":
        print("Ending program.")
        break
    else:
        print("Must choose between 1, 2, 3 or 4.")


"""The program as I have made it above does what the assignement wants. 

Things that could be added though;

-A way to take the same kinds of inputs to remove a child incase one gets sick 
or something. Might be slightly unneccesary since its easy to start it 
over and run it again.
-A way to change the prices through input. Could be good during times of 
inflation, like now, when supermarkets are raising prices daily. Or one could
show the user the way to simply change the variables in the program itself. Could
be done for the package size of the sausages aswell.
"""