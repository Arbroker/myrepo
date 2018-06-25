#******************************************************************************
# interest.py
#******************************************************************************
# Name: Armend Lulani
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used): 
# Ben & you, prof., for giving me useful hints for the challenge. 
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# Program to calculate compound interest using formula A = P*e^(r*t)
# Where t = 2, and user inputs percent rate and principal amount.
# Challenge hint: variables can be reused

import math

principal = float(input("Enter a principal amount: "))

rate = float(input("Enter first interest rate: "))*(.01) #converting percent to decimal
A = principal*math.exp(rate*2)                         #Compound interest formula

rate = float(input("Enter second interest rate: "))*(.01)
principal = A*math.exp(rate*2)                      #reassigning principal to... 
                                                    #...calculate new account balance
rate = float(input("Enter third interest rate: "))*(.01)
A = principal*math.exp(rate*2)                      #same switcharoo method...
                                                    #...to meet challenge req.
rate = float(input("Enter fourth interest rate: "))*(.01)
principal = A*math.exp(rate*2)

rate = float(input("Enter fifth interest rate: "))*(.01)
A = principal*math.exp(rate*2)                      

print("The final value is: ${0:.2f}".format(A))

