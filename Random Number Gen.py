#Joe Joseph

#Intro to Programming

import random

# Random number game

# Function

def main():

#Counter
    t = 0
# Ask user for input
    guess = int(input('Please enter a number between 1 and 100: ' , ))
# Set 1-100 parameters
    number = random.randint(1, 100)

# Start loop for high, low, and correct guess
    
    while (number != guess):
            if guess > number:
                t = int(t + 1)
                guess = int(input('To high, try again: ' ,))
            if guess < number:
                t = int(t + 1)
                guess = int(input('Too low, try again: ',))
            if guess == number:
                break
            
# print message and add together all the guesses
            
    if guess == number:
                t = str(t + 1)
                print('Congratulations, It took you ' + t +  ' guesses ' + 'and the number was ' , guess)
            
                
# Repeat function
    return main()

main()












    
