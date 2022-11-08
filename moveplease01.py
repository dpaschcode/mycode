#!/usr/bin/env python3

""" Script for renaming files and moving them"""

#Import required modules
import shutil
import os

def main():
    
    #Perform required move
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # Program apuse to accest data
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()
