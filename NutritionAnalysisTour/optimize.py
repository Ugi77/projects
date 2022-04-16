# -*- coding: utf-8 -*-

"""
Author: Dima (Ugi77)

Description: 
This code inputs a prepared file of drink names & nutritional values, and 
creates Drink objects to hold this info.  Then, the maxiumum drinks one can 
obtain (with a given calorie constraint) is output, based upon which value is 
considered optimal: calories, caffeine, fats, or sugars.

Note: 
This code was adapted from the MITx 6.00.2x Introduction to Computational Thinking 
and Data Science course.  The basic structure originates from a lecture example, 
and this was then modified to input a file, optimize a set of data with different 
parameters, and output results in a new way.

How to play:

"""

import csv

filename = open('sb_prep.csv', 'r')
file     = csv.DictReader(filename)

name_list = []
cal_list  = []
caff_list = []
fat_list  = []
sug_list  = []
 
# Iterate over each .csv row, append values to lists
# Cast nutritional values as floats, then integers
for col in file:
    name_list.append(col['prep_name'])
    cal_list.append(int(float(col['calories_%dv'])))
    caff_list.append(int(float(col['caffeine_%dv'])))
    fat_list.append(int(float(col['fat_%dv'])))
    sug_list.append(int(float(col['sugars_%dv'])))
 
# print('Name:', name_list)
# print('Calories:', cal_list)
# print('Caffeine:', caff_list)
# print('Fat:', fat_list)
# print('Sugars:', sug_list)


# Class: Drink
# Description: represents nutritional values of a drink item
class Drink(object):
    
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name: a string, the drink name, size, and milk type
    #   cal:  an integer, the %DV calories in a drink 
    #   caff: an integer, the %DV caffeine in a drink
    #   fat:  an integer, the %DV fats in a drink 
    #   sug:  an integer, the %DV sugars in a drink        
    # Precondition: none
    # Returns: A newly created object of type Drink
    def __init__(self, name, cal, caff, fat, sug):
        # Data attributes: 
        #   name: a string, the drink name, size, and milk type
        #   cal:  an integer, the %DV calories in a drink 
        #   caff: an integer, the %DV caffeine in a drink
        #   fat:  an integer, the %DV fats in a drink 
        #   sug:  an integer, the %DV sugars in a drink 
        self.name = name
        self.cal  = cal
        self.caff = caff
        self.fat  = fat
        self.sug  = sug
        
    # Method: get_cal
    # Description: retrieves the calorie %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: an integer         
    def get_cal(self):
        return self.cal

    # Method: get_caff
    # Description: retrieves the caffeine %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: an integer   
    def get_caff(self):
        return self.caff

    # Method: get_fat
    # Description: retrieves the fat %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: an integer    
    def get_fat(self):
        return self.fat

    # Method: get_sug
    # Description: retrieves the sugar %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: an integer        
    def get_sug(self):
        return self.sug
    
    # Method: __str__
    # Description: Defines how to cast the objects of class Drink into a string.  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        return self.name

# test = Drink("expresso", 3, 4, 5, 6)
# result = test.get_sug()
# print(test)
# print(result)

## END OF CLASS DRINK ##


# Function: build_menu 
# Description: takes in lists of drink features, generates a list of Drink objects
# Parameters: 
#     name_list: a list of strings, of drink names, sizes, and milk types
#     cal_list:  a list of integers, of calorie %DV values
#     caff_list: a list of integers, of caffeine %DV values
#     fat_list:  a list of integers, of fat %DV values
#     sug_list:  a list of integers, of sugar %DV values
# Returns: a list of Drink objects
def build_menu(name_list, cal_list, caff_list, fat_list, sug_list):
    menu = []
    for i in range(len(name_list)):
        # Create a Drink object with a list element from name_list, cal_list, etc. at iterated index position
        # Add each Drink object to the menu list
        drink_obj = Drink(name_list[i], cal_list[i], caff_list[i], fat_list[i], sug_list[i])
        menu.append(drink_obj)
    return menu

drink_menu = build_menu(name_list, cal_list, caff_list, fat_list, sug_list)
# for item in drink_menu:
#     print(item)


# Function: greedy 
# Description: generates the maximized 'best' drinks one can take, based on available 
#              calories and preferred value (sugar, caffeine, etc.) 
# Parameters: 
#     drink_menu:   a list of Drink objects
#     max_cals:     an integer >= 0, representing maximum available calories to take
#     key_function: getter method call to Drink, to define ordering of Drink objects 
#                   by what is considered the 'best' feature (e.g. caffeine, sugars)
# Returns: None
def greedy(drink_menu, max_cals, key_function):
    # Use sorted fxn to create a copy of the items list
    # Specify key so sort is based on what to consider as the best feature
    # Then reverse the copied list to sort best to worst
    drink_menu_copy = sorted(drink_menu, key = key_function, reverse = True)
    taken_items = []
    total_cal, total_caff, total_fat, total_sug = 0, 0, 0, 0
    
    # For each sorted Drink object, going best to worst...
    for i in range(len(drink_menu_copy)):
        # Call get_cal method to get calories 
        # If these calories, plus total calories are less than or equal to max_cal,
        # (e.g. is there room to take item?), add to taken_items and add values to running totals
        # If greater than max_cal value, go to next Drink obj
        if (total_cal + drink_menu_copy[i].get_cal()) <= max_cals:
            taken_items.append(drink_menu_copy[i])
            total_cal  += drink_menu_copy[i].get_cal()          
            total_caff += drink_menu_copy[i].get_caff()
            total_fat  += drink_menu_copy[i].get_fat()
            total_sug  += drink_menu_copy[i].get_sug()
    
    # Output results
    for item in taken_items:
        print('   ', item)
    print('         ')
    print('Total drink %DV for...')
    print('Calories:', total_cal)
    print('Caffeine:', total_caff)
    print('Fats:    ', total_fat)
    print('Sugars:  ', total_sug)
    print('*************')
    
# greedy(drink_menu, 10, Drink.get_caff)
