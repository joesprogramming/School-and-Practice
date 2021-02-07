# Joe Joseph
#Febuary days

# Ask user to input Year

year = int(input('Enter a year and this program will tell you how many days Febuary will have. ' ,))

#Calculate divisibility

if year % 100 == 0 and year % 400 == 0:
    print('Febuary has 29 days in', year)
elif year % 100 != 0 and year % 4 == 0:
    print('Febuary has 29 days in', year)
else:
    print('Febuary has 28 days in', year)
