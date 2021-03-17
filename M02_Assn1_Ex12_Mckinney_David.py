# David Ryan McKinney
# SDEV140 M02_Assn1 Ex12
# 1/26/2021 11am
# V1.0
# Software Volume Discount Calculator
# quantityOrdered (int) quantity of software ordered
# discountDec (float) discount percent as decimal

# discountAmt (float) discount amount in $USD
# softwareCost (int) cost of software package
# totalDiscount (float) total savings
# finalPrice (float) price after discounts


# Welcome message for user
print("Hello consumer. Thank you very kindly for choosing DRM Enterprises for your software needs.")
print("We have a sliding scale discount, depending on the quantity ordered.")
quantityOrdered = int(input("How many packages would you like to order? "))
# assigning software package cost
softwareCost = 99
#calculating subtotal
subtotal = (softwareCost * quantityOrdered)
# calculating discount percentage
if quantityOrdered < 10:
    discountDec = 0.0
elif quantityOrdered < 20:
    discountDec = 0.10
elif quantityOrdered < 50:
    discountDec = 0.20
elif quantityOrdered < 100:
    discountDec = 0.30
elif quantityOrdered >= 100:
    discountDec = 0.40
    
#calculating total discount
totalDiscount = (subtotal * discountDec)
#calculating finalPrice
finalPrice = (subtotal - totalDiscount)

#User display screen of total calculations
print("Quantity of Software Purchases: ", quantityOrdered)
print("Pre-Discount Total: $", subtotal)
print("Discount Percentage: ", (discountDec * 100), "%" )
print("Discount :", totalDiscount)
print("Final Sale Price: $", finalPrice)
