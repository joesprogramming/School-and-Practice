

# Joe Joseph

# Intro to programming

# Pet class program

import pet



def main():

    name_pet = input('Enter the pets name: ')
    animal_type = input('Enter the pets type: ')
    animal_age = input('Enter the pets age: ')

# create instance of Pet class

    data = pet.Pet(name_pet, animal_type, animal_age)

    # Display the data that was entered

    print('The pets name is: ' , data.get_name())
    print('The pets type is: ' , data.get_a_type())
    print('The pets age is: ' , data.get_age())

# call function

main()
