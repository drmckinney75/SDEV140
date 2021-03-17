#David McKinney
#Sales Tax Calculator
#SDEV140 M01-Assn2-Ex6
#Program designed to compute state tax, county tax, and total purchase price
#State tax is 5%
#County Tax is 2.5%
#purchase (float) amount of purchase
#stateTax (float) amount of state tax from purchase
#countyTax (float) amount of county tax from purchase
#totalTax (float) amount of total tax from purchase
#totalSale (float) total of purchase and taxes

print('Hello user. This program is designed to help you calculate sales tax on purchases.')
#prompting user for purchase price
purchase = float(input('Please enter purchase price. '))
#calculating taxers and storing as variables
stateTax = (purchase * 0.05)
countyTax = (purchase * 0.025)
totalTax = (stateTax + countyTax)
totalSale = (purchase + totalTax)
print(f'This purchase in total is ${totalSale:.2f}.')
print(f'Your State taxed you ${stateTax:.2f}.')
print(f'Your County taxed you ${countyTax:.2f}.')
print(f'In total, you paid {totalTax:.2f} in taxes.')
print('Thanks for using this program, and helping me learn python!')


def main():
    calc_state_tax(purchase):
    calc_county_tax(purchase):
    calc_total_tax():
    calc_total_sale():
print(f'This purchase in total is ${totalSale:.2f}.')
print(f'Your State taxed you ${stateTax:.2f}.')
print(f'Your County taxed you ${countyTax:.2f}.')
print(f'In total, you paid {totalTax:.2f} in taxes.')
print('Thanks for using this program, and helping me learn python!')

def calc_state_tax(purchase):
    stateTax = (purchase * 0.05)

def calc_county_tax(purchase):
    countyTax = (purchase * 0.025)

def calc_total_tax(  