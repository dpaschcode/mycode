#!/usr/bin/env python3

""" My first API call python script"""

##  install required modules
import requests

# define the URL for the API call
uri = 'https://pokeapi.co/api/v2/pokemon/'

# make a lookup to the URI
response = requests.get(uri + 'pikachu')
# GET /api/v2/pokemon/pikachu  --------------------->  https://pokeapi.co:443
#                              <---------------------  200 "OK" + json

# ensure reciept of a 200 response
if response.status_code != 200:
        print("Uh oh! a non-200 status code was returned.", response.status_code)
        exit()


response_json = response.json()

print(response_json.get("name"))
print(response_json.get("id"))
