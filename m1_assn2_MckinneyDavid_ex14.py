#David McKinney
#Compound Interest Calculator
#SDEV140 M01-Assn2-Ex14
#Program designed to calculate compound interest
#P (float) principal amount originally deposited
#r (float) annual interest rate
#n (float) number of times per year interest is compounded
#t (float) specified number of years
# prompting user for loan details to calculate and output
P = float(input('Enter principal amount: $'))
r = float(input('Enter annual interest rate % '))
n = float(input('Enter number of times per year interest has compounded: '))
t = float(input('Enter number of years account will be left to earn interest: '))

#moving decimal point to correct position
r /= 100 # 50% = .50

A = P * ((1 + (r / n))**(n * t))
#output results according to user input
print('After ', t, ' years, $', format(A, ',.2f'), ' will be in the account. ', sep='')