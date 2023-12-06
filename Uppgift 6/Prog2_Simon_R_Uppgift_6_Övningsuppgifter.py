# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pd
rad = "              "



# 12.1: Let user pick which to print.

notes = {"Meddelande från skolan": "Friluftsdag på tisdag.",
         "Kom ihåg": "Ta bilen till verkstad.",
         "Inför tentamen": "Gör alla instuderingsuppgifter."}

dict_print = input("Pick > ")
if dict_print in notes:
    print(notes[dict_print])
else:
    print("There is no such note.")

# 12.2: Use a for loop to print the keys (Titles).
print(rad)
notes = {"Meddelande från skolan": "Friluftsdag på tisdag.",
         "Kom ihåg": "Ta bilen till verkstad.",
         "Inför tentamen": "Gör alla instuderingsuppgifter."}
print("*"*20, "\n", "Notes".center(20))
for i in notes:
    print(i)

# 12.3: Use a for loop to print keys and values.
print(rad)
notes = {"Meddelande från skolan": "Friluftsdag på tisdag.",
         "Kom ihåg": "Ta bilen till verkstad.",
         "Inför tentamen": "Gör alla instuderingsuppgifter."}

print("*"*20, "\n", "Notes".center(20))
for i in notes:
    print("Titel;", i, "\nText;", notes[i])

# 12.4: Allow user to add something to the notes and then print it out.
print(rad)
notes = {"Meddelande från skolan": "Friluftsdag på tisdag.",
         "Kom ihåg": "Ta bilen till verkstad.",
         "Inför tentamen": "Gör alla instuderingsuppgifter."}

print("What would you like to add?")
titel = input("Titel; > ")
text = input("Text; > ")
if titel not in notes:
    notes[titel] = text
else:
    print(f"{titel} already in notes.")
print("*"*20, "\n", "Notes".center(20))
for i in notes:
    print("Titel;", i, "\nText;", notes[i], "\n")

# 12.5: Allow user to remove a thing from the notes.
print(rad)
notes = {"Meddelande från skolan": "Friluftsdag på tisdag.",
         "Kom ihåg": "Ta bilen till verkstad.",
         "Inför tentamen": "Gör alla instuderingsuppgifter."}

choice = input("Which do you want to remove? > ")
if choice in notes:
    notes.pop(choice)
else:
    print(f"{choice} is not in notes.")
print(notes)











