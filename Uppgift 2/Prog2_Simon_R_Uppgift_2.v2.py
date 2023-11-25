#Could make a simpler version as well;

import math

# Prices here so user can change it if needed;
normal_cost = 20.95
vegan_cost = 34.95
soda_cost = 13.95

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
        normal_packs = math.ceil(normal_amount / 8)
        vegan_packs = math.ceil(vegan_amount / 4)
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

"""After making this one, I think this one is more accurate actually.. 
Its simple, doesn't crash and outputs in a similar manner to the way 
christian åberg has it in the compendium. 
Takes less input. Don't need to dick around with a menu. Could simply 
run the program all over again if anything needs to be changed amongst 
the input from the user.
"""