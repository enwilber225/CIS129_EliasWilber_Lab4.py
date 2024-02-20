#
# declare local variables 

monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
print()
print("----")
print()
prompt = "What is monthly sales?: $ "
prompt2 = "What is increase in sales?: $ "
prompt3 = "What is store bonus?: "
prompt4 = "What is employee bonus?: $ "
prompt5 = "Total Results: $ "
print("----")

# Get input values

monthlySales = float(input(prompt))
salesIncrease = float(input(prompt2))
storeBonus = float(input(prompt3))
empAmount = float(input(prompt4))

# Calculate result and output

total_amount = monthlySales + salesIncrease + storeBonus + empAmount
print()
print(prompt5, total_amount)
print()
print()
# this code determines the storeAmount bonus
print()
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: 
    print("There will be no bonus this period")

# this code gets the percent of increase in sales

salesIncrease = float(input(prompt2))
salesIncrease = salesIncrease / 100

# this code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    print("the employees do not get a bonus")

# this code prints the bonus information

print("The store bonus amount is: $", storeBonus)
print("The employee bonus amount is: $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print("congrats! you have reached the highest bonus amounts possible!")





