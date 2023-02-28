##################################################
# Mike Solie                                     #
# CYBR-260-40                                    #
# 02/12/2023                                     #
# Week 5                                         #
# Version 1.4                                    #
# Writing to Windows Registry                    #
#                                                #
# Description:                                   #
# Takes user input and writes it to a            #
# predetermined key in Windows Registry. It also #
# writes the time when run and current working   #
# directory into the same key.                   #
##################################################

# take input from user and write to reg key
# store current time as value inside new key
# get current working directory - dir/ls

#####
# import os - To get the curret working directory
# import winreg - To interact with Windows Registry
# import datatime - To write the date/time of when the program was run to the registry
#####
import os
import winreg
from datetime import datetime

#####
# function: date_time
# purpose: to store the date/time of when the program was run to a variable
# inputs: none
# returns: time
#####
def date_time():
    # variable that stores time
    time = datetime.now()
    # returns the variable for main
    return time

#####
# function: pwd
# purpose: to get and store the current working directory in a variable
# inputs: none
# returns: current working directory
#####
def pwd():
    # variable to store current working directory
    my_cwd = os.getcwd()
    # returns current working directory for main
    return my_cwd

#####
# function: new key
# purpose: to create a new key in Windows registry and give it values
# inputs: The location of the registry to write, key name, date/time, current working directory, and user input
# returns: the data and its location written in the registry
#####
def new_key(key_name, sub_key, value):
    # try block, if the key is already created (or some other error) will output reason for error
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\' + key_name)
        winreg.SetValueEx(key, str(sub_key), 0, winreg.REG_SZ, str(value))
    except Exception as ex:
        print(f'Could not write input {ex}')

#####
# function: main
# purpose: to run the program
# inputs: user input
# returns: nothing, runs the program
#####
def main():
    # user input for subkey
    input_subkey = str(input('What is the subkey?: '))
    # user input for the value of the subkey
    input_value = str(input('What is the text value of the subkey?: '))
    # time function output transformed into a string
    time = str(date_time())
    # pwd function output transformed into a string
    cwd = str(pwd())

    # name of the new key to write to the registry - location defined in new key
    key_name = 'NewKey'
    # calls new_key and writes user input
    new_key(key_name, input_subkey, input_value)
    # calls new_key and writes time
    new_key(key_name, "time", time)
    # calls new_key and writes cwd
    new_key(key_name, "cwd", cwd)


# call to start the program
##---->
main()
##<----
# program end
