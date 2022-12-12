# Kahan Shah 
# simplebudgeter.py
# This code asks the user for their budget and baased on how much the user has spent tells the user if they are overbudget or not.
# Acknowledgement: https://www.w3schools.com/python/python_conditions.asp 

# Ask user for name using input
name = input ("Please enter your name ")

# Greet the user using print and name variable
print ("Hello", name + " I hope you are well.")

# Ask user how much is their budget using input. Use float to accomodate decimals.
budget = float (input ("How much is your budget in dollars? "))

# Use print to confirm tha budget amount 
print("Your budget is $", budget)

# Ask user how much is they have spent using input. Use float to accomodate decimals.
cashspent = float (input("How much have you already spent in dollars "))

# Use if else statement to tell user if they went over the budget or not. If they didn't use subtraction to show extra money left. If they did use subtraction to tell how much they overspent. And print the results.
if budget >= cashspent:
    extracash = budget - cashspent
    print("You have not gone over your budget. You have $",extracash)

else:
    budget < cashspent
    overspent = cashspent - budget
    print("You have sadly gone over your budget by $",overspent)

