#David McKinney
#Sales Tax Calculator
#SDEV140 M03_Assn1Ex2
#Program designed to compute state tax, county tax, and total purchase price
#State tax is 5%
#County Tax is 2.5%

#purchase (float) amount of purchase
#stateTax (float) amount of state tax from purchase
#countyTax (float) amount of county tax from purchase
#totalTax (float) amount of total tax from purchase
#totalSale (float) total of purchase and taxes


totalTax = 0.0


def main():
    print('Hello user. This program is designed to help you calculate sales tax on purchases.')
    #prompting user for purchase price
    purchase = float(input('Please enter purchase price. '))
    # passing purchase amount to state tax module
    stateTax = calc_state_tax(purchase)
    # total tax assignment
    # # couldn't get it to run without assigning this here # # 
    totalTax = 0.0
    # adding tax total
    totalTax = totalTax + stateTax
    # passing purchase to county tax module
    countyTax = calc_county_tax(purchase)
    # again calculating total tax
    totalTax = totalTax + countyTax
    # calling total sale module
    totalSale = calc_total_sale(purchase, totalTax)
    # user friendly summary display
    print(f'This purchase in total is ${totalSale:.2f}.')
    print(f'Your State taxed you ${stateTax:.2f}.')
    print(f'Your County taxed you ${countyTax:.2f}.')
    print(f'In total, you paid ${totalTax:.2f} in taxes.')
    print('Thanks for using this program, and helping me learn python!')

    

# calculates state taxes
def calc_state_tax(price):
    stateTax = (price * 0.05)
    return stateTax
# calculates county tax    
def calc_county_tax(price):
    countyTax = (price * 0.025)
    return countyTax
# calculates total sales price
def calc_total_sale(price, taxes):
    totalSale = (price + taxes)
    return totalSale


main()