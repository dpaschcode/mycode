#!/usr/bin/env python3

""" Lab 40: Exploring network interfaces """

## import required modules
import netifaces

## Open main Funciton
def main():
    ## loop through the interfaces and collect info
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
                print('Could not collect adapter information')

## Print our net intercaes
#    print(netifaces.interfaces())


main()
