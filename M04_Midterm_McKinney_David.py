## David Ryan McKinney
## SDEV140
## M04_Midterm2
## 2/14/21
## Sentence capitalization
## Program designed to take user input and format the sentence with punctuation
## and capitalized first word.

## prompting user for input
my_string = input('Enter a sentence: ')
new_string = ''
## capitalizing first word
new_string += my_string[0].upper()
## setting accumulator
i = 1
## checking for multiple sentences
while i < len(my_string)-2:
    new_string += my_string[i]
    if my_string[i] == '.' or my_string[i] == '?' or my_string[i] == '!':
        new_string += ' '
        new_string += my_string[i+2].upper()
        i = i+3
    else:
        if i == len(my_string)-3:
            new_string += my_string[len(my_string)-2:len(my_string)]
        i = i+1
## Adding a period
new_string += '.'
list = new_string.split()
## user friendly output
print(new_string)
print('There are ' , len(list) , ' words in the sentence.')
