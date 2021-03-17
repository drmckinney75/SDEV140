#Calculating Factorials
#David Ryan McKinney
#SDEV140 M02 Assn2 Ex12
#program written to calculate nonnegative integer factorial
# num (int) user input number to calculate factorials
#factorial (int) start of factorial calculations (1 -> user input)
#i (int) iterations counter
print("Welcome user. Calculate Factorials With Ease!")
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not compute with negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
    # calculating >0 factorial
   for i in range(1,num + 1):
       factorial = factorial*i
       print(i,"subtotal: ",factorial)
   print("The factorial of",num,"is",factorial)