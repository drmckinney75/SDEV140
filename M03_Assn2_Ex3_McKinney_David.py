## David Ryan McKinney
## SDEV140
## M03_Assn2_Ex3
## 2/5/21
## Monthly Step Counts
## Takes an input from a CSV file and averages steps taken per month

## the top portion was my first attempt


## lets pc know how many days are in a month for accurate calculations
def getDays(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


## processes steps for entire month, month by month
def processMonth(month):
    days = getDays(month)
    total = 0
    for day in range(1, days + 1):
        line = int(file.readlines().rstrip(','))
        total += line
    average = total / days
    print(getMonth(month), '=', format(average, '.0f'))


## assigns numeric date to traditional month names
def getMonth(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'

## this part was explained to me by a friend
## i couldn't figure out how to modulate such a small code

def main():
    print('Step Tracker Data Analysis')
    print('David Ryan McKinney')
    
    file = open('mysteps.txt', 'r')
    month_steps = dict()
    walked_days = dict()
    for line in file.readlines():
        year, month, day, steps = line.split(",")
        if int(year) == 2020:
            month, day, steps = int(month), int(day), int(steps)
            walked_days[month] = walked_days.get(month, 0) + 1
            month_steps[month] = month_steps.get(month, 0) + steps

    for month in range(1, 13):
        print(f"Actual average for {getMonth(month)}: {month_steps[month] / walked_days[month]:.2f}")
        print(f"Average based on days in month for {getMonth(month)}: {month_steps[month] / getDays(month):.2f}")
        print(f"Actual days walked for {getMonth(month)}: {walked_days[month]:.2f}")

main()
