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

# Prices here so user can change them if needed;
normal_cost = 20.95
vegan_cost = 34.95
soda_cost = 13.95

# Package sizes here so they can be changed if needed;
normal_pkg_size = 8
vegan_pkg_size = 4

inputs = {"normal": 0, "vegan": 0}
while True:
    print("  .:Korvkollen:.")
    print("-" * 20)
    print("How many kids want.. ")
    # try excepts incase one is invalid input.
    try:
        normal_2 = int(input("2 normal sausages? > "))
        normal_3 = int(input("3 normal sausages? > "))
        vegan_2 = int(input("2 vegan sausages? > "))
        vegan_3 = int(input("3 vegan sausages? > "))
        # adding the amounts together;
        normal_amount = (normal_2 * 2) + (normal_3 * 3)
        vegan_amount = (vegan_2 * 2) + (vegan_3 * 3)
        amount_soda = normal_2 + normal_3 + vegan_2 + vegan_3
        # Splitting amounts on pkg size.
        normal_packs = math.ceil(normal_amount / normal_pkg_size)
        vegan_packs = math.ceil(vegan_amount / vegan_pkg_size)
        total = ((normal_packs * normal_cost) + (vegan_packs * vegan_cost) + (amount_soda * soda_cost))
        print("-" * 20)
        print("Shopping list; ")
        print(f"Normal sausage packs; {normal_packs}")
        print(f"Vegan sausage packs; {vegan_packs}")
        print(f"Amount of sodas; {amount_soda}")
        print(f"Total price; {total}")
        break
    except:
        print("Need to input a whole number.")

""" 
One thing that wasn't required from the assignment that could be useful is the
ability to change the prices, could be solved by showing end user how to
change it in the program ofc but I think it would be better through input.
Same thing with the sizes of the packages for the sausages.
"""