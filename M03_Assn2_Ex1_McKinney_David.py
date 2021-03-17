## David Ryan McKinney
## SDEV140
## M03_Assn2_CustEx1
## 2/3/21
## This program asks a user to input the quantity of random numbers
## We create a file with this many numbers in it
## We then read from the file to determine the highest, lowest, and average
## Displaying results to the user

## Super challenging for me, but i feel awesome having finished this
## The 24/7 tutor couldn't pinpoint my error but i tinkered until it worked!

import random
## writing file with user input
def write():
    object_file = open('random_numbers.txt', 'w')
    how_many = int(input('Enter a number to determine how many random numbers'
                          '\n the file will hold: '))
    for i in range(how_many):
        number = random.randrange(10, 500)
        number = str(number)
        object_file.write(number)
        object_file.write('\n')
    object_file.close()

## manipulating file created
def read():
## setting accumulator value and beginning total and highest value variables
    count = 0
    total = 0
    highest = 0
    ## if i didnt indicate this then I would never get lower than zero
    ## which is what I did at first
    lowest = 501
    try:
        object_file = open('random_numbers.txt', 'r+')
        for i in object_file:
            total += int(i)
            count += 1
            if int(i) > highest:
                highest = int(i)
            else:
                if int(i) < lowest:
                    lowest = int(i)
                else:
                    lowest = lowest
    ## IO error flag         
    except IOError:
        print('IOError')
    ## Value error flag
    except ValueError:
        print('ValueError')
     ## user friendly output  
    print('Sum : ', total)
    print('Items : ', count)
    print('Average : ' ,(total / count))
    print('Highest : ', highest)
    print('Lowest : ', lowest)
    object_file.close()


## Main module
def main():
    print('Welcome to the Random Number Manipulator.')
    print('We will create a file with random integers,')
    print('and perform calculations with the output.')
    write()
    read()

main()
