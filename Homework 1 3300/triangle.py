#******************************************************************************
# triangle.py
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
# Program to compute the angles of an SSS triangle 
# using the Law of Sines & Cosines 

import math

a = float(input("Enter the largest sidelength: "))
b = float(input("Enter the middle sidelength: "))
c = float(input("Enter the smallest sidelength: "))

if not(a>0 and b>0 and c> 0):   
    print("Error: Your lengths are not all positive!")
elif a<b<c or b<a<c:           
    print("Error: Your lengths are not in descending order!")
if not(a+b>c and a+c>b and b+c>a): #Triangle Inequality
    print("Error: Your lengths don't satisfy the triangle inequality!")
else:
    
    a_ang = math.acos((-(a*a) + b*b + c*c)/(2*b*c)) #Law of cosines 
    a_deg = math.degrees(a_ang)                     #Converting to degrees

    b_ang = math.degrees(math.asin((b*(math.sin((a_ang)))/a)))  #Law of sines

    c_ang = 180 - (a_deg + b_ang)                   #Finding smallest angle
    print("The angles are: ")
    print(a_deg)
    print(b_ang)
    print(c_ang)
    