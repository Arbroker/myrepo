#******************************************************************************
# monopoly.py
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
# Program to simulate a game of monopoly... if two dice rolls match, roll again
# ...if they match 3 times in a row, go to jail! 
# challenge: No nested ifs

import random

def roll(n):
    """ function which returns a random integer x: 1<=x<7 """
    r_1 = random.randrange(1,7)
    return r_1

p = roll(1) #variables to represent dice rolls 1 - 6
q = roll(2)
r = roll(3)
x = roll(4) 
y = roll(5)
z = roll(6)

if not(p == q):                                 # if the first pair don't match,
    print("First roll is:",p,q)                 #display them...
    print("Move {0} spaces".format(p+q))        #...and their sum
elif not((p==q) and (r==x)):                    #if the second pair don't match
    print("First roll is:",p,q)         
    print("Second roll is:",r,x)
    print("Move {0} spaces".format(p+q+r+x))
elif ((p==q) and (r==x) and (y==z)):            #if all three pairs match (Jail)
    print("First roll is:",p,q)
    print("Second roll is:",r,x)
    print("Third roll is: ",y,z)    
    print("GO TO JAIL CHEATER!")                
else:                                           #Otherwise, display the case...
    print("First roll is:",p,q)                 #...where the third pair doesn't match.
    print("Second roll is:",r,x)
    print("Third roll is: ",y,z)
    print("Move {0} spaces".format(p+q+r+x+y+z))