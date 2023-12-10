# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

import requests
import json

# 13.1:

try:
    number = int(input("Type a whole number > "))
    url = 'https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=' + str(number)
    r = requests.get(url)
    response_dict = r.json()
    print(response_dict)
    len_factor = len(response_dict['factors'])
    print(len_factor)
    fac = response_dict['factors']
    if len_factor <= 1:
        print(f"{number}'s factor is {response_dict['factors']}")
    elif len_factor == 2:
        print(f"{number}'s factors are {response_dict['factors'][0]} and {response_dict['factors'][1]}.")
    elif len_factor > 2:
        factors = ""
        length = 0
        while length < (len_factor - 2):
            factors += str(response_dict['factors'][length]) + ", "
            length += 1
        print(f"{number}'s factors are; " + factors + str(fac[-2]) + " and " + str(fac[-1]) + ".")
    if response_dict['even'] == True and response_dict['prime'] == True:
        print(f"{number} is even. And it is a prime number.")
    elif response_dict['even'] == False and response_dict['prime'] == True:
        print(f"{number} is not even. But it is a prime number.")
    elif response_dict['even'] == True and response_dict['prime'] == False:
        print(f"{number} is even. But it is not a prime number.")
    else:
        print(f"{number} is neither even nor a prime number.")
except ValueError:
    print("ValueError. Must input a whole number.")

# 13.2:

def letters(city):
    city_new = ""
    for i in city:
        if i == "ö":
            city_new += "o"
        elif i == "å" or i == "ä":
            city_new += "a"
        else:
            city_new += i
    city = city_new
    return city

def get_info(city):
    cities = ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Västerås"]
    if city in cities:
        if city in ["Göteborg", "Malmö", "Västerås"]:
            city = letters(city)
    else:
        print("Can't find data for this city.")
    url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower()
    r = requests.get(url)
    city_dict = r.json()
    for i in city_dict['forecasts']:
        print(i['date'] + " - " + i['forecast'])
while True:
    city = input("Which city do you want a forecast for? > ").capitalize()
    print("*"*20)
    print(city + " forecasts;")
    print("*"*20)
    get_info(city)
    break

