# Joe Joseph
# Program 4

#Calculate compound interest

# Ask for original principal that was deposited


print('Hello, this program will calculate the compound interest the account will earn over its lifetime.')
principal = float(input('Enter the original principal you deposited: ' , ))

# Ask what the annual interest rate is

interest = float(input('What is your interest rate (enter a whole number): ' ,)) / 100

# print(interest)

# Ask how often the interest is compounded

times = int(input('How many times is the interest compounded: ', ))

# Ask the number of years the account will be left to earn interest

years = int(input('Enter the number of years the account will be left to earn interest: ', ))

# Calculate and dispaly account value

total = principal * (((1 + (interest / times)) ** (times * years)))

# print account value after the specified number of years

print('The total value of your account will be %s after %d years.' % (total, years))
