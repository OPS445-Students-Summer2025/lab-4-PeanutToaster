#!/usr/bin/env python3
#Author: Ricky Tang
#ID: 104448246

def is_digits(sobj):
    # place code here - loop through each character in sobj
    digits = set('0123456789') #sets the digits to check during the loop
    check = 0
    #start the check at index 0
    length = len(sobj) #set length to the length of the input sobj
    while check < length: #while to stop after checking all indexes
        for i in sobj: # for loop to check all characters for digits
            if i not in digits:
                return False # return false if character is not in the variable set of digits
            check = check + 1 # check next character
    return True #if all checked + in digits, return true for main program

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')