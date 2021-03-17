## David Ryan McKinney
## SDEV140
## M03_Assn2_Ex2
## 2/5/21
## Number File Analyzer
## Takes a text file and displays numbers while indicating
## non numeric entries, tabulating input types







def main():
    print('Hello user. Prepare to have your socks knocked off.')
    print('We are going to analyze your badnumbers.txt')
    print('and deduce if there is any non numeric data.)
    print('----------------------------------------------------')
    print('File Read Exceptions - David Ryan McKinney')
    
    goodnumbers = 0
    badnumbers = 0
    file = open('badnumbers.txt', 'r')
    for line in file.readlines():
        try:
            line = float(line)
            print (line)
            goodnumbers += 1
        ## Value error flag
        except ValueError:
            print('Non numeric data')
            badnumbers += 1
          
    print('Amount of good numbers: ', goodnumbers)
    print('Amount of bad numbers: ', badnumbers)


main()
    
