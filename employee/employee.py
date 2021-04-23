

# Joe Joseph

# Intro to programming

# Class

class Employees:

    def __init__(self, name, number):

        self.__name = name

        self.__number = number
                 

    def set_name(self, name):

        self.__number = name
        

    def set_unit_i(self, number):

        self.__number = number

    


#Methods

    def get_name(self):

        return self.__name
        

    def get_number(self):

        return self.__number

class production_worker(Employees):

    def __init__(self, shift, pay):

        Employees.__init__(self, shift, pay)
        

        self.__shift = shift

        self.__pay = pay

    def day_shift(self):

        if self.__shift == '2':
            
            print('Night Shift')

        else:
            print('Day Shift')

    
    def get_shift(self):

        return self.__shift

    def get_pay(self):

        return self.__pay

        
        

    


