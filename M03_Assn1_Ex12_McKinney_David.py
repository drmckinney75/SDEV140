## Numberdome
## David Ryan McKinney
## SDEV 140
## M03_Assn1_Ex12
## Evaluates two user input values and displays the larger value
## 2/1/21



## number comparison function
## taking input from main module input and comparing
## displays whether one is higher 
## or if numbers are equal
def number_comparison(a, b):
    if (a > b):
        print("{0} is Greater than {1}".format(a, b))
    elif (b > a):
        print("{0} is Greater than {1}".format(b, a))
    else:
        print("Both a and b are Equal")



def main():
    ## user input
    print('Welcome To Numberdome!')
    print('Two numbers enter...')
    print('One number leaves!')
    a = float(input(" Please Enter the First Value: "))
    b = float(input(" Please Enter the Second Value: "))
    number_comparison(a, b)


main()        