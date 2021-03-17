## David Ryan McKinney
## SDEV140
## M04_Ex_1
## 2/9/21
## Sales Data Manipulator
## Takes input as sales per day, calculate total sales and average
## daily sales for week

## list of days for user friendly display
DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']		 

## accepting input of sales
def salesinput():
    ## declaring empty list to store daily sales
    sales_for_week = [0, 0, 0, 0, 0]		
    ## for loop collecting sales numbers			 
    index = 0
    print('Please enter the sales for each work day:')
    while index < len(sales_for_week):
        sales_for_week[index] = int(input( DAYS_OF_WEEK[index]+ ' : '))
        index += 1
    return sales_for_week	

def calculations(salesinfo):	  
	
	## calculating total and using that to get average
    total = sum(salesinfo)
    average = total/(len(salesinfo))	 
    return average, total

def output(average, total, salesinfo):
    ## user friendly output
    print('Here are the sales for the week:')
    ## for loop to display daily sales
    for i in range(5):	 
        print(DAYS_OF_WEEK[i], ' :  ', salesinfo[i])
    print('------------')
    ## printing total and average numbers
    print('TTL: ', total)
    print('Avg:  ',average)


def main():
    ## runs input module to receive sales list
    salesinfo = salesinput() 
    ## getting total and average from calculation module
    average, total = calculations(salesinfo)
    ## running output module to display results
    output(average, total, salesinfo)	 
    
    
main()
