#Ask user to input a number

# Intro to Programming

# Ask for user to input a whole number and save then number as the integer variable

integer = int(input('If you enter a whole number (1-10). This program will convert it to a Roman Numeral: ' ,))


#Test inputed value against and generate Roman Numeral

if integer == 1:
    print('I')
elif integer == 2:
    print('II')
elif integer == 3:
    print('III')
elif integer == 4:
    print('IV')
elif integer == 5:
    print('V')
elif integer == 6:
    print('VI')
elif integer == 7:
    print('VII')
elif integer == 8:
    print('VIII')
elif integer == 9:
    print('IX')
elif integer == 10:
    print('X')
    
# If interger is outside of requested range print an error.

if integer < 1:
    print('That number is less than 1')
else:
    if integer > 10:
        print('That Number is greater than 10')



    
