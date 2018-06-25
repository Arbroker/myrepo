#******************************************************************************
# parks.py
#******************************************************************************
# Name: Armend Lulani
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): NONE
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# A program which asks the user for a location, and comparing it to 3 given parks...
# ... prints which park is closest (in Kms) to the given location

import math

lat = float(input("Enter a latitude: "))
long = float(input("Enter a longitude: "))

cnt_lat = 40.782800 
cnt_lng = -73.965269
pr_lat = 40.660217
pr_lng = -73.968948
fl_lat = 40.739694
fl_lng = -73.840793

def distance(lt_one,lng_one,lt_two, lng_two):
    """ Function which finds the distance between user-inputted set of 
        lattitude and longitute, and given set of center of 3 parks """
    lt_chg = lt_one - lt_two                #∆Lat
    lng_chg = lng_one - lng_two             #∆Long
    lt_deg = lt_chg*111.048                 #Convert to kms
    lng_deg = lng_chg*84.515                #conver to kms
    dist = math.sqrt((lt_deg*lt_deg)+(lng_deg*lng_deg)) # Distance formula 
    return dist

x = distance(lat,long,cnt_lat,cnt_lng) #distance between input values and central park vals
y = distance(lat,long,pr_lat,pr_lng) #distance between input and Prospect park
z = distance(lat,long,fl_lat,fl_lng) #distance between input and Flatbush park


if x>y>z or y>x>z:      #distance between user input and Flatbush park is least, print:
    print("Flatbush Meadows Corona park is the closest park, with a distance of,",z,"km")
elif y>z>x or z>y>x:    #distnace between input and Central park is least, print:
    print("Central park is the closest park, with a distance of,",x,"km")
elif z>x>y or x>z>y:    #ditance between input and Prospect park is least, print:
    print("Prospect park is the closest park with distance of,",y,"km")
    