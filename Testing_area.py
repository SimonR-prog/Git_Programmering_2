teams = [{
        "country": 'Brazil',
        'wins': 4,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0}]




#print("{:^4} {:^4} {:^4}".format(v,v,v))

num = 1
print("-" * 40)
print("| # |", " Nation".ljust(14), "| W | D | L | GF | GA | GD | P |" )
print("-" * 40)
for i in teams:
    txt = "{:<14} {:^4} {:^4} {:^4} {:^4} {:^4} {:^4} {:^4}"
    nation = i["country"]
    w = i["wins"]
    d = i["draws"]
    l = i["losses"]
    gf = i["goals_for"]
    ga = i["goals_against"]
    gd = int(gf) - int(ga)
    p = (int(w) * 3) + int(d)
    print(f"| {num} |", txt.format(nation, w, d, l, gf, ga, gd, p))
