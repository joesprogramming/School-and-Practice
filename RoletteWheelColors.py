# Roulette wheel
# Joe Joseph
# Intro to Programming

# Ask for user input

integer = int(input('Welcome! Please enter a number 0-36 and this program will tell you if that pocket is green,red, or black: ' ,))

#Determine if integer is odd or even. Assign correct color to the determined outcome
if integer == 0:
    print('green')
elif integer >=1 and integer <= 10:
    if integer % 2 and integer !=0:
        print('red')
    else:
        print('black')
elif integer >=11 and integer <= 18:
    if integer % 2 and integer !=0:
        print('black')
    else:
        print('red')
elif integer >=19 and integer <=28:
    if integer % 2 and integer !=0:
        print('red')
    else:
        print('black')
elif integer >=29 and integer <=36:
    if integer % 2 and integer !=0:
        print('black')
    else:
        print('red')
#Print error statement
if not(integer >=0 and integer <=36):
    print('Please enter a number between 0-36')
