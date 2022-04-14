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
    print(col)
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

