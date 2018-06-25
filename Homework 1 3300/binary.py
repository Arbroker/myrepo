#******************************************************************************
# binary.py787
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
# Program which converts an 8 digit binary number into decimal 
# and converts a decimal number x: 0<=x<=255, to binary 

number = (input("Enter an 8 digit binary number: "))

#Algorithm to convert: d_7*(2^7) + d_6*(2^6) +...+ d_1*(2^1) + d_0*(2^0)

one = int(number[0]) * (2**7)           #first digit is multiplied by 2^7                 
two = int(number[1]) * (2**6)           
three = int(number[2]) * (2**5)
four = int(number[3]) * (2**4)  
five = int(number[4]) * (2**3)          #           ,,,
six = int(number[5]) * (2**2)
seven = int(number[6]) * (2**1)  
eight = int(number[7]) * (2**0)         #last digit is multiplied by 2^0

decimal = one + two + three + four + five + six + seven + eight     #adding...

print("The binary number {0} is the same as the decimal number {1}".format(number,decimal))

#challenge
integer = int(input("Now, enter an integer between 0 and 255: "))

if integer > 255:          #If statement to ensure the program runs only when... 
                           #...input < 256 otherwise program prints erroneously for > 255
                           
    print("Error: That integer is not in the specified range!")
    

#using a modified version of the division algorithm to get the necessary remainder values
else:
    r_one = (integer)%2           # Finding first remainder when dividing by 2
    q_one = (integer)//2          # Finding first quotient using floor division            
    r_two = q_one%2               # Finding next remainder when dividing quotient by 2        
    q_two = q_one//2
    r_three = q_two%2                 
    q_three = q_two//2                 
    r_four = q_three%2                   
    q_four = q_three//2                         
    r_five = q_four%2              #               ...
    q_five = q_four//2
    r_six = q_five%2
    q_six = q_five//2
    r_sev = q_six%2
    q_sev = q_six//2
    r_eig = q_sev%2                # Since input is <= 255, only need 8 remainders
    print(str(r_eig)+str(r_sev)+str(r_six)+str(r_five)+str(r_four)+str(r_three)+str(r_two)+str(r_one))

#above ugly print statement returns the remainders as a number with no spaces 
#remainders in descending order (r_n,r_n-1,...,r_1,r) is the input converted to binary. 


