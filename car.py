
# Joe Joseph

# Intro to programming

#Car Class

#define clase

class Car:
    
    def __init__(self, year, make, speed):
        
        self.__year = year
        
        self.__make = make
        
        self.__speed = 0


# Model attribute
        
    def set_year(self, year):

        self.__year = year

# Make attribute
    def set_make(self, make):

        self.__make = make

# speed attribute

    def set_speed(self, speed):

        self.__speed = 0

        
    def get_year(self):

        return self.__year


    def get_make(self):

        return self.__make


    def get_speed(self):

        return self.__speed

#Class methods

    def acc(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        
        return self.__speed

        
    

