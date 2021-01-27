#Joe Joseph
#Chapter 2 Ex 8 Program 3

# Calculate total amount of a meal Purchased
# Ask for total cost for the meal

meal = float(input('Enter the cost of the meal and this program will calculate the tip, tax, and total cost: ', ))

# print (meal)

# Calculate Tip

tip = meal * .18

# Calculate tax

tax = meal * .07

# Calculate total

total = tip + tax + meal

# Display Tip,Tax, and Total

print('The recommended tip is:', tip)
print('The meals tax is:', tax)
print('The total cost of the meal is:', total)
