
#Joe Joseph

#Intro to programming

#Car Class program


# Import class

import car


#Create function 

def main():

#Create loop value

    x = 0

# Ask for user input
    
    year_py = input('Enter the year of the vehicle: ')
    make_py = input('Enter the Make of the vehicle: ')
    speed_py = print('Your current speed is 0')
    


    #instance of class
    
    veh = car.Car(year_py, make_py, speed_py)
# Loop to accelerate
    for x in range (5):
        print('The model is', veh.get_make())
        veh.acc()
        print(veh.get_speed())
        x=x+1
        
#Loop to Brake
        
        if x == 5:
          for x in range (5):
            print('The mode is', veh.get_make())
            veh.brake()
            print(veh.get_speed())
            x=x+1

main()
