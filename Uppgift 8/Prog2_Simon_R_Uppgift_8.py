# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

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
    """
    Function takes input in the form of team names and an integer as scores.
    Function will then add the scores to the value of the keys depending on results."""

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

# 14.5:
def make_list(dict):
    """
    Function takes the previous dictionary and makes it into a list while
        turning the country name into the value of a "country"-key.
    Returns updated dictionaries inside a list."""
    list = []
    for i in dict:
        teams_2 = {}
        teams_2["country"] = i
        teams_2.update(dict[i])
        list.append(teams_2)
    teams = list
    return teams

# 15.3:
def sort_list(list):
    """
    Function uses a for loop to add a new key with the points calculated as value.
    Uses lambda in place of another function to return the dict["points"] value
        to be able to use the sorted function.
    Returns a list of teams sorted by the points made with the highest points at the top."""
    for i in list:
        points = (int(i["wins"]) * 3) + int(i["draws"])
        i["points"] = points
    teams_list_sorted = sorted(list, key=lambda dict: dict["points"], reverse=True)
    return teams_list_sorted

# 14.6:
def print_table(list):
    """
    Function takes input in the form of a list of dictionaries.
    Uses a formatted string (txt) to first print out the header.
    Then uses a for loop to print the dictionaries in the list."""
    width = 47
    num = 1
    txt = "{:<12}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|"
    print("-" * width)
    print("| # |", txt.format("Nation","W","D","L","GF","GA","GD","P"))
    print("-" * width)
    for i in list:
        nation = i["country"]
        w = i["wins"]
        d = i["draws"]
        l = i["losses"]
        gf = i["goals_for"]
        ga = i["goals_against"]
        gd = int(gf) - int(ga)
        p = (int(w) * 3) + int(d)
        print(f"| {num} |", txt.format(nation, w, d, l, gf, ga, gd, p))
        num += 1
    print("-" * width)

# 15.3:
add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

teams_list = make_list(teams)
teams_list_sorted = sort_list(teams_list)
print_table(teams_list_sorted)





"""
print("-"*40)
print(teams)
print("-"*40)
print(teams_list)
print("-"*40)
print(teams_list_sorted)
"""