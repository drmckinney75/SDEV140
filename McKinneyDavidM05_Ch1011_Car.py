## David Ryan McKinney
## SDEV140
## M04_Ex_3
## 2/9/21
## Car Class Creation
## First foray into creating classes

class Car:
## Accepts car's year model and make as arguments
    def __init__(self,year,make):
        self.__year_model = year
        self.__make = make
        ## starting speed is zero
        self.__speed = 0
    
    def accelerate(self):
    ## increases speed by 5 each time it is called
        self.__speed += 5
    
    def brake(self):
    ## decreases speed by 5 each time it is called
        self.__speed -= 5
    
    def get_speed(self):
    ## returns the current speed
        return self.__speed