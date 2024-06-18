# Cash Register Simulator
#
# Ask the user to input (scan) the barcode and enter the price and quantity of the item.

import re
import sys

# Prompt user for barcode
upc= input("Please enter the 12 digit barcode: ")

# Check to make sure input is 12 numbers, without characters
if not re.match("^\\d{12}$", upc):
    print("Must enter 12 numbers. No characters allowed.")
    sys.exit()

#Print various parts of UPC code in order
print(upc[0],upc[1:6],upc[6:11],upc[11])

#Define cost of each unit
cost = input("Please enter the price of this item: $")

# Check to make sure the correct format is used for entering price
if not re.match("^\\d+(\\.\\d{2})?$", cost):
    print("Invalid price! Please enter in USD format.")
    sys.exit()

#Define how many units looking to purchase
amount = input("Please enter the quantity of this item: ")

# Check to make sure the correct format is used for entering price
if not re.match("^[1-9]\\d*$", amount):
    print("Invalid amount! Please enter a valid quantity.")
    sys.exit()

#Calculate total cost for purchasing 12 units
costTOTAL=(float(cost)*int(amount))

#Final calculations of amount, unit cost and total cost  
print("To purchase {0} units, each costing ${1:,.2f}, the total will be ${2:,.2f}.".format(amount, float(cost), costTOTAL)) 
