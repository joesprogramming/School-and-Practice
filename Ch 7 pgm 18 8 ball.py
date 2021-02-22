# Joe Joseph

# Intro to Programming

# 8 Ball

import random

#define function

def main():

    # Ask user for a question

    input('Hello! I am a Python 8 ball. Ask me a question: ' ,)

    # open file

    
    infile = open('8ball.txt', 'r')



    # Call random line from a file
    read = random.choice(infile.readlines())

    # Close file

    
    infile.close()


    print(read)

    # Loop to ask player if they want to continue
    
    ask = input('Do you want to keep playing Y/N? ')
    while ask == ('Y'):
        return main()
    else:
        print('Have great day')
    
    
main()


