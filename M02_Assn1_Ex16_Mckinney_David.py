# David Ryan McKinney
# SDEV140
# M02_Assn1_Ex16
# 1/26/21 11:45am
# v1.0
# Program written to identify leap years and display number of days in February based on user input
# yearInput (int) year input by user to determine leap year status
# daysInFeb (int) number of days in Feb in user selected year

# welcome display
print("Hello comrade. Welcome to DRM Enterprises Leap Year Calculator.")
print("The premiere State Sponsored Leap Year Software Solution.")
print("How will YOU use your extra day?")
#asking for year to begin calculations
yearInput = int(input("Please enter a year to test:  "))
#checking leap year status
if yearInput > 0:
    
    if yearInput % 100 == 0:
        #first leap year test
        if yearInput % 400 == 0:
            daysInFeb = 29
        else:
            daysInFeb = 28
    else:
        # possible leap year
        if yearInput % 4 == 0:
            daysInFeb = 29
        else:
            daysInFeb = 28
else:
    print("Invalid year entered. Please run program again.")
#leap year selectionstructure to determine output for user
if daysInFeb >= 29:
    print("", yearInput, " is a leap year!")
    print("February of ", yearInput, " has 29 days.")
else:
    print(yearInput, " is not a leap year.")
    print("February of ", yearInput, " has 28 days.")
    