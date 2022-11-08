#!/usr/bin/env python3
""" if, elif, else - Ice cream shop Lab."""


def main():

    message1 = 'Hello!, Weilcome to the ice cream buffet!\n '
    message2 = 'Call Weight Watchers!!! '

    # Gather user input and float to accept decimals as numbers
    scoops = float(input("How many scoops do you want?"))

    # Analyze scoops for reply message
    if scoops == 1:
        message = message1 + 'Here is your ' + str(scoops) + ' scoop.'
    elif scoops == 2:
        message = message1 + 'enjoy your ' + str(scoops) + '  scoops!.'
    elif scoops == 3:
        message = message1 + str(scoops) +'!!! Enough for a growing man!!!.'
    elif scoops > 3:
        message = message2
    print(message)

main()
