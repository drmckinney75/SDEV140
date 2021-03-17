# David Ryan McKinney
# SDEV140
# M02_Assn1_Ex16
# Wifi Diagnostic Tool
# v1.0
#Program designed to guide user through Wi Fi problem diagnosis


# global variables
stdQuestion = 'Did that fix the problem? Please type y or n (lower case): '
Q1 = 'Reboot the computer and try to connect.'
Q2 = 'Reboot the router and try to connect.'
Q3 = 'Make sure the cables between the router and modem are plugged in firmly.'
Q4 = 'Move the router to a new location.'
Q5 = 'Get a new router'
CONGRATS = 'Congratulations!'
# welcome message for user
print("Welcome to DRM Industries' WiFi Diagnostics")
print("Where your problems, are somehow, our problems.")
#first test
print(Q1)
userAnswer = input(stdQuestion)
if userAnswer == "n" or userAnswer =="N":
    print(Q2)
    userAnswer = input(stdQuestion)
    if userAnswer == "n" or userAnswer =="N":
            print(Q3)
            userAnswer = input(stdQuestion)
            if userAnswer == "n" or userAnswer =="N":
                    print(Q4)
                    userAnswer = input(stdQuestion)
                    if userAnswer == "n" or userAnswer =="N":
                            print(Q5)
                    else:
                            print(CONGRATS)
            else:
                        print(CONGRATS)
    else:
                print(CONGRATS)
else:
        print(CONGRATS)
                            
                            
                        

                    
            
            
        
    
    