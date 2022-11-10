#!/usr/bin/env python3

""" Lab 42 work """

# Import call from subprocess
from subprocess import call

def main():

    # Call your interface details
    call(["ip", "link", "show", "up"])

    # Print the output of the interface call
    print("This program will check your interfaces.")

    # ask again with a specific interface, give example
    interface = input("Enter an interface, like, ens3: ")
    call(["ip", "addr", "show", "dev", interface])
    call(["ip", "route", "show", "dev", interface])

main()

