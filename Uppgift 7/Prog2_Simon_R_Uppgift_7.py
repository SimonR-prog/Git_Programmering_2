# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

import requests
import json

"""
Define what we need to do in no order;
Print the list of the available artists to chose from.
Take an input from user for which artist.
Extract the id number for that artist, send it to another function that prints the artist info.

Output;


"""








url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
r = requests.get(url)
artist_list = r.json()
print(artist_list)

"""
url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' + id
r = requests.get(url)
city_dict = r.json()
"""














