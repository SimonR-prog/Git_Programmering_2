# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 14.1:

"""Make function that, based on input, turns km into miles and vice versa."""

def transfer(amount, string):
    if string.lower() == "miles":
        return int(amount) * 1.609344
    elif string.lower() == "km":
        return int(amount) * 0.621371192
    else:
        print("Invalid input.")
try:
    transform = input("Amount and current measurement. > ")
    x = transform.split()
    print(transfer(x[0],x[1]))
except:
    print("")

# 1.609344 miles to km
# 0.621371192 km to miles

def miles_km(distance):
    return distance * 1.609344

def km_miles(distance):
    return distance * 0.621371192

distance = input("Distance and measurement. > ").lower()
dis_split = distance.split()
if dis_split[1] in ["km", "miles"]:
    if dis_split[1] == "km":
        print(f"{distance} is;", km_miles(float(dis_split[0])), "miles.")
    else:
        print(f"{distance} is;",miles_km(float(dis_split[0])), "km.")


# 14.3:
import random
def get_even(list):
    even = []
    for i in list:
        if i%2 == 0:
            even.append(i)
    return even

numbers = []
for x in range(10):
    numbers.append(random.randint(0,9))
even = get_even(numbers)
print(numbers)
print(even)


# 14.4:

teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    }
}


def add_game(home_team, home_score, away_team, away_score):
    teams[home_team]["goals_for"] += home_score
    teams[home_team]["goals_against"] += away_score
    teams[away_team]["goals_for"] += away_score
    teams[away_team]["goals_against"] += home_score
    if home_score == away_score:
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1
    elif home_score > away_score:
        teams[home_team]["wins"] += 1
        teams[away_team]["losses"] += 1
    else:
        teams[away_team]["wins"] += 1
        teams[home_team]["losses"] += 1

add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
add_game ("Brazil", 2, "Costa Rica", 0)
add_game ("Serbia", 1, "Switzerland", 2)
add_game ("Serbia", 0, "Brazil", 2)
add_game ("Switzerland", 2, "Costa Rica", 2)


for i in teams:
    print(i, teams[i])


# 14.5:

# Take the dictionary above and make it so that the team names are the value of a key.
# Each team and its result is going to be a dictionary. All of them gathered in a list.

list = []

for i in teams:
    teams[i]["country"] = i
    list.append(teams[i])

print(list)














