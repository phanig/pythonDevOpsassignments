"""04/04/2017
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use raw_input to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.
Output:
96.25
"""

h=raw_input("Enter number of hours worked:")
r=raw_input("Enter rate per hour:")
p=int(h)*float(r)
print p
