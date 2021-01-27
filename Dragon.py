import random
import time

def displayIntro():
    print('''Welcome to dragon hell. You see two caves in front on you.
one leads to victory and the other to death''')
    print()
def chooseCave():
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you enter? (1 or 2)')
        cave = input()

    return cave
def checkCave(chosenCave):
    print('Your approach the cave....')
    time.sleep(2)
    print('It is dark')
    time.sleep(2)
    print('A large dragon leaps forward!')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('You have chosen to live')
    else:
        print('You embrace deaths cold grapse')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
