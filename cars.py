# Help someone decide if they should buy a car

# Price of vehicle
price = int(input("What is the price of the vehicle? $"))

# New or used?
type = input("Is this a new or used car? ")

# How many months would they like to finance?
months = int(input("Choose how many months you would like your financing to be: 36, 48, 60, 72, or 84: "))

# Calculate APR
if (type == 'new'):
    if(months == 36):
        apr = 1.9
    elif(months == 48):
        apr = 2.9
    elif(months == 60):
        apr = 3.9
    elif(months == 72):
        apr = 4.9
    elif(months == 84):
        apr = 5.9

else:
    if(months == 36):
        apr = 7.0
    elif(months == 48):
        apr = 7.5
    elif(months == 60):
        apr = 8.5
    elif(months == 72):
        apr = 9.0
    elif(months == 84):
        apr = 9.5

downPayment = int(input("How much are you putting down? $"))
newPrice = price - downPayment
# Calculate monthly payment
monthlyPayment = float(newPrice * (((apr/(12*100))*(1+(apr/(12*100)))**months) / (((1+(apr/(12*100)))**months) - 1)))

print("Financing a {0} car at ${1} for {2} months will give you a {3}% interest rate. You will pay ${4:.2f} per month" .format(type, price, months, apr, monthlyPayment))