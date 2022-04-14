import csv

filename = open('sb_prep.csv', 'r')
file     = csv.DictReader(filename)

name = []
cal  = []
caff = []
fat  = []
sug  = []
 
# iterate over each .csv row, append values to lists
# cast nutritional values as floats
for col in file:
    name.append(col['prep_name'])
    cal.append(int(float(col['calories_%dv'])))
    caff.append(int(float(col['caffeine_%dv'])))
    fat.append(int(float(col['fat_%dv'])))
    sug.append(int(float(col['sugars_%dv'])))
 
# print('Name:', name)
# print('Calories:', cal)
# print('Caffeine:', caff)
# print('Fat:', fat)
# print('Sugars:', sug)

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
        return self.name + ' %DV: ' + str(self.cal) + ' cal, ' + str(self.caff) + ' caff, ' + str(self.fat) + ' fat, ' + str(self.sug) + ' sug' 

# End of class Drink

test = Drink("expresso", 3, 4, 5, 6)
result = test.get_sug()
print(test)
print(result)