## David Ryan McKinney
## SDEV140
## M04_Ex_3
## 2/9/21
## Interacting with Car class
## Calls the class Car and returns information
import McKinneyDavidM05_Ch1011_Car

Car = McKinneyDavidM05_Ch1011_Car.Car('2004','Porsche')
## Plugged in our vehicle for testing
## calls accelerate module in Car class 5 times
for x in range(5):
    Car.accelerate()
    ## prints speed every call
    print('Current speed is', Car.get_speed())
## calls decelerate modules in Car class 5 times
for y in range(5):
    Car.brake()
    ## prints speed after every call
    print('Current speed is', Car.get_speed())
