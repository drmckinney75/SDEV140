## David Ryan McKinney
## SDEV140
## M04_Ex_2
## 2/9/21
## Popular Baby Names
## Program to allow user to search for names within popular baby
## name list, boys and girls

## global lists
boy_names = open("boynames.txt")
girl_names = open("girlnames.txt")
boys = []
girls = []


def main():
    ## user friendly splash screen
    print('Search Popular Baby Names')
    print('David Ryan McKinney')
    ## getting boys and girls lists back from files processed
    ## in readFiles()
    boys, girls = readFiles()
    ## passing user selection and name inquiry from getUserInputs()
    user_input, gender = getUserInputs()
    ## using values returned to search lists and display results
    search(user_input, gender, boys, girls)
    

## get input from user
def getUserInputs():
    gender_select = input('Enter a "b" to search boy names or a "g" to search girl names (or "x" to exit):')
    if gender_select == 'b':
        user_input = input('Enter a name to search for: ')
    elif gender_select == 'g':
        user_input = input('Enter a name to search for: ')
    else:
        print('Thanks for playing!')
    return user_input, gender_select

## reading files and putting into lists
def readFiles():
    global boys
    global girls
    boys = boy_names.read().splitlines()
    girls = girl_names.read().splitlines()
    return boys, girls



def search(user_input, gender, boys, girls):
    ## if/else for 'b' selection
    if gender == 'b':
        if user_input in boys:
        	rank = boys.index(user_input)
            print(user_input , 'was #' , rank , 'in popular boys names.')
        else:
            print('Sorry, ', user_input , 'was not in the Top 200 Popular Boys Names.')       
    else:
        ## if/else for 'g' selection
        if user_input in girls:
        	rank = girls.index(user_input)
            print(user_input , 'was #' , rank , 'in popular girls names.')
        else:
            print('Sorry, ', user_input , 'was not in the Top 200 Popular Girls Names.')
            
    
main()
