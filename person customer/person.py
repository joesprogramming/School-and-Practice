#Joe Joseph

# Intro to Programming


#Primary Class

class Person:

    def __init__(self, name_p, address_1, phone_1):

        self.__name_p = name_p

        self.__address_1 = address_1

        self.__phone_1 = phone_1

    def set_name_p(self, name_p):

        self.__name_p = name_p

    def set_address_1(self, address_1):

        self.__address_1 = address_1

    def set_phone_1(self, phone_1):

        self.__phone_1 = phone_1

# Methods


    def get_name_p(self):

        return self.__name_p

    def get_address_1(self):

        return self.__address_1

    def get_phone_1(self):

        return self.__phone_1

#Subclass

class Customer(Person):

    def __init__(self, name, mail):

        self.__name = name

        self.__mail = mail

#Boolean Function

    def list_mail(self):


#Loop for mailing list

        if self.__mail == 'Y':

            print('Welcome to the mailing list')

        else:

            print('You have been removed')

    def get_name(self):

        return self.__name

    def get_mail(self):

        return self.__mail






    
    
