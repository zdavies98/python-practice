# The ATM Machine Problem
#
# Ask the user how much they would like to withdraw from the atm, then calculate how many of each bill type they will receive

# Ask user for the amount to withdraw
withdrawAmount = int(input("How much would you like to withdraw?: "))

# initialize variables
count1 = 0
count5 = 0
count10 = 0
count20 = 0
count100 = 0

# Calculate how many of each bill needed
while (withdrawAmount >= 100):
    withdrawAmount -= 100
    count100 += 1
    
while (withdrawAmount >= 20):
    withdrawAmount -= 20
    count20 += 1
    
while (withdrawAmount >= 10):
    withdrawAmount -= 10
    count10 += 1
    
while (withdrawAmount >= 5):
    withdrawAmount -= 5
    count5 += 1

count1 = withdrawAmount
    

# Print the outcome
print("We have released {0} $100 bills, {1} $20 bills, {2} $10 bills, {3} $5 bills, {4} $1 bills.".format(count100, count20, count10, count5, count1))
