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

#Putting variables outside of while loop so that they can be added to and don't
#reset or generate a new number everytime it loops.
rand = random.randint(1,99)
guess = 0

while True:
    try: #Try except to catch user not inputting a intger.
        choice = int(input("Pick a number between 1 and 99. > "))
        if choice >= 1 and choice <= 99: #Making sure player has guessed between 1 and 99..
            if choice == rand:
                guess += 1 #Increasing the guess variables value by 1 every correct type of guess.
                print(f"Congrats!\nThe right number was {rand}.\nYou guessed {guess} times.")
                break #Closign while loop.
            elif choice > rand: #If players choice is higher than the random number.
                print("Need to guess lower.")
                guess += 1
            elif choice < rand: #If players choice is lower than the random number. 
                print("Need to guess higher.")
                guess += 1
        else:
            print("Must choose a number between 1 and 99.")
    except:
        print("Must enter a whole number.")
    

#Another version made while doing assignement 4..

rand = random.randint(1,99)
guess = 0

while True:
    try:
        choice = int(input("Pick a number between 1 and 99. > "))
        if choice > 0 and choice < 100:
            guess += 1 #Increasing the guess variables value by 1 every correct type of guess.
            if choice != rand:
                if choice > rand: #If players choice is higher than the random number.
                    print("Need to guess lower.")
                elif choice < rand: #If players choice is lower than the random number. 
                    print("Need to guess higher.")
            else:
                print(f"Congrats!\nThe right number was {rand}.\nYou guessed {guess} times.")
                break #Closign while loop.
        else: 
            print("Must pick a number between 1 and 99.")
    except:
        print("Need to type a whole number.")
    

























