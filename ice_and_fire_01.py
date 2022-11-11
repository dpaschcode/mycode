#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    """Ask user for input"""
    got_char_to_lookup = input("Pick a number between 1-1000 to return info on a GoT character! ")

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_char_to_lookup, timeout = 10)

    ## Decode the response
    got_dj = gotresp.json()
    pprint.pprint(got_dj)

if __name__ == "__main__":
    main()
