#Nested Loop Pattern Display
#SDEV140
#M02_Assn2_Ex14
#David Ryan McKinney
#program written to display a pattern using nested loops
#welcome message
print("Hello user. Prepared to have your mind blown?")
print('DRM Enterprises Nested Loop Pattern Display')
#setting the starting line pattern
n = 7
#loops to display pattern with decreasing characters down to 1
for b in range (0,11):
    n = n - 1
    for d in range (0, n+1):
        print ('*', end = '')
    print()
print ('')
