

# Joe Joseph

# Intro to programming

# Class

class RetailItem:

    def __init__(self, item_d, unit_i, price_r):

        self.__item_d = item_d

        self.__unit_i = unit_i

        self.__price_r = price_r
                 

    def set_item_d(self, item_d):

        self.__item_d = item_d
        

    def set_unit_i(self, unit_i):

        self.__unit_i = unit_i
        

    def set_price_r(self, price_r):

        self.__price_r = price_r


#Methods

    def get_item_d(self):

        return self.__item_d
        

    def get_unit_i(self):

        return self.__unit_i
        

    def get_price_r(self):

        return self.__price_r


