#!/usr/bin/env python3

""" script for Tuesday challenge"""

def main():

    # user to provide input
    user_firstname = input("first Name:")
    user_lastname = input("last name:")
    user_favnumber = input("favorite number:")
    

    # list1 = []      # "declaring"
                      # list1 exsits and is the type list, but has a "zero value" (its empty)
    # list1.append(x) # "initalization" - list1 has values the following "non-zero"
    #
    # 
    # delcare & initalize at the same time
    list1 = [(user_firstname), (user_lastname), (user_favnumber)]

    # display info back to the user.
    print(list1)

main()
