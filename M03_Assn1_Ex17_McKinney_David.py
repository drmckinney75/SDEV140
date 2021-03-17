## David ryan McKinney
## SDEV140
## M03_Assn1_Ex17/Ex18
## 2/1/21



# prompt user for value and return it as a variable 'x'
def get_value():
    return int(input('Please enter a positive integer: '))

# check if the number is prime
def is_prime(x):
    # When x <= 1 False is returned
    if x <= 1:
        return False
    else:
        # When x = 2, True is returned
        i = 2
        while x > i:
            # If x % == 0, it shows 'False', otherwise i = i + 1 while x > i.
            if x % i == 0:
                return False
            else:
                i = i + 1
        else:
            return True

def print_result(boolean):
    print('Is the value you entered Prime?')
    print(boolean)

def main():
               
    x = get_value()

    boolean = is_prime(x)

    print_result(boolean)

main()