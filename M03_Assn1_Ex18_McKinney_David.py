## Prime Number List (1-100)
## David Ryan McKinney
## SDEV140
## 2/1/21
## M03_Assn1_Ex18
## Uses function to display prime numbers between 1 - 100


def is_prime():
    print('All prime Numbers between 1 and 100')
    print('Challenging but fulfilling exercise!')
    print('David Ryan McKinney')
    n = 1
    for n in range(2, 101):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
        if prime == True:
            print(n)
            

is_prime()
