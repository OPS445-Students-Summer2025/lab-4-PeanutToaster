#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    new_dict = {}
    for index in range(len(keys)): #for each index in the range of the length of the variable keys
        new_dict[keys[index]] = values[index] #set new_dict variable to the index of the keys
    return new_dict # return the dictionary 
    # Can also use while loop
    '''
    result = {}
    index = 0
    while index < len(keys):
        new_dict[keys[index]] = values[index]
        index += 1
    return new_dict
    '''

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    dict1_values = set(dict1.values())
    dict2_values = set(dict2.values())
    return dict1_values & dict2_values

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)