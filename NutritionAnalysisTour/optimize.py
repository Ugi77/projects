import csv

filename = open('sb_prep.csv', 'r')
file     = csv.DictReader(filename)

name_list = []
cal_list  = []
caff_list = []
fat_list  = []
sug_list  = []
 
# iterate over each .csv row, append values to lists
# cast nutritional values as floats
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
# Description: represents aspects of a drink item
class Drink(object):
    
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name: type string, a drink
    #   cal:  type float, %DV calories in a drink 
    #   caff: type float, %DV caffeine in a drink
    #   fat:  type float, %DV fat in a drink 
    #   sug:  type float, %DV sugars in a drink        
    # Precondition: none
    # Returns: A newly created object of type Drink
    def __init__(self, name, cal, caff, fat, sug):
        # Data attributes: 
        #   name: type string, a drink
        #   cal:  type float, %DV calories in a drink 
        #   caff: type float, %DV caffeine in a drink
        #   fat:  type float, %DV fat in a drink 
        #   sug:  type float, %DV sugars in a drink 
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
    # Returns: a float         
    def get_cal(self):
        return self.cal

    # Method: get_caff
    # Description: retrieves the caffeine %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float    
    def get_caff(self):
        return self.caff

    # Method: get_fat
    # Description: retrieves the fat %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float    
    def get_fat(self):
        return self.fat

    # Method: get_sug
    # Description: retrieves the sugar %DV of a Drink object
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float         
    def get_sug(self):
        return self.sug
    
    # Method: __str__
    # Description: Defines how to cast the objects of class Drink into a string.  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        # return self.name + ' %DV: ' + str(self.cal) + ' cal, ' + str(self.caff) + ' caff, ' + str(self.fat) + ' fat, ' + str(self.sug) + ' sug' 
        return self.name

# End of class Drink

# test = Drink("expresso", 3, 4, 5, 6)
# result = test.get_sug()
# print(test)
# print(result)

# Function: build_menu 
# Description: takes in lists, generates a list of Drink objects
# Parameters: 
#     name_list: a list of strings, of drink names
#     cal_list:  a list of floats, of calorie %DV values
#     caff_list: a list of floats, of caffeine %DV values
#     fat_list:  a list of floats, of fat %DV values
#     sug_list:  a list of floats, of sugar %DV values
# Returns: a list of Drink objects
def build_menu(name_list, cal_list, caff_list, fat_list, sug_list):
    menu = []
    for i in range(len(name_list)):
        # create a Drink object with a list element from name_list, cal_list, etc. at iterated index position
        # add each Drink object to the menu list
        drink_obj = Drink(name_list[i], cal_list[i], caff_list[i], fat_list, sug_list[i])
        menu.append(drink_obj)
    return menu

drink_menu = build_menu(name_list, cal_list, caff_list, fat_list, sug_list)
for item in drink_menu:
    print(item)