"""Higher lower;
Defining assignement;

-Generate a random number as value for a variable.
-Count how many guesses the player does.
-If guess is too high or too low, print a message which way they need to go.

Output;
-How many guesses they took in the end.
-What the correct number was.
-Wether they need to go higher or lower.
"""

#Importing random to generate the random number.
import random

# Random variable outside loop to only generate once.
rand = random.randint(1,99)
guess = 0
valid_range = range(1,100)
while True:
    try: # Try loop to catch invalid input, valueerror.
        choice = int(input("Pick a number between 1 and 99. > "))
        # If choice in the range between 1 and 99;
        if choice in valid_range:


            # increasing for every valid guess;
            guess += 1
            if choice != rand:
                if choice > rand: #If players choice is higher than the random number.
                    print("Need to guess lower.")
                else: #If players choice is lower than the random number.
                    print("Need to guess higher.")
            else: #Correct guess;
                print(f"Congrats!\nThe right number was {rand}.\nYou guessed {guess} times.")
                break
        else: 
            print("Must pick a number between 1 and 99.")
    except:
        print("Need to type a whole number.")
    

























