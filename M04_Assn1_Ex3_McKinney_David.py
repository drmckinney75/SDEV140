## David Ryan McKinney
## SDEV140
## M04_Ex_3
## 2/9/21
## Character Analysis
## Program designed to count uppercase, lowercase, punctuation, and white space
## in a text file, as well as a total character count.

## declaring global access to sampletext file
## could simply change filename to any txt desired to gather statistics
SAMPLE = open("sampletext.txt")

def main():
    ##user friendly splash screen
    print('Analyze Text File Characters!')
    print('David Ryan McKinney')
    ## getting file contents from filetolist module
    list =filetolist()
    ## running list through counter module, returning results
    upper, lower, digits, space, punct = counter(list)
    ## putting results into output module
    display(upper, lower, digits, space, punct)
    

def filetolist():
    ## reading file and storing in list for manuipulation
    lines = SAMPLE.read().splitlines()
    return lines

def counter(lines):
    ## declaring local variables as integers, = 0
    upper = 0
    lower = 0
    digits = 0
    space = 0
    punct = 0
    ## interating each line
    for line in lines:
        ##iterating each character
        for ch in line:
            ## adds count if uppercase
            if ch.isupper():
                upper += 1
            ## adds count if lowercase
            elif ch.islower():
                lower += 1
            ## adds count if digits
            elif ch.isdigit():
                digits += 1
            ## adds count if space
            elif ch.isspace():
                space += 1
            ## adds count if punctuation
            else:
                punct += 1
    ## returning counts for file characters
    return upper, lower, digits, space, punct

## displays results in a user friendly format
def display(upper, lower, digits, space, punct):
    print('Results: ')
    print('Characters : ', (upper + lower + digits + space))
    print('Uppercase : ', upper)
    print('Lowercase : ', lower)
    print('Digits : ', digits)
    print('Whitespace : ', space)
    print('Punctuation : ', punct)
    
## calls main() into action
main()
