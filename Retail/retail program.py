

# Joe Joseph

# Intro to programming

import retail1


def main():

    #variables

    item_d1 = retail1.RetailItem('Jacket', '12', '59.95')

    item_d2 = retail1.RetailItem('Designer Jeans', '40', '34.95')

    item_d3 = retail1.RetailItem('Shirt', '20', '24.95')



    print('Description Units in Inverntory Price')
    print('--------------------------------------')
    print(item_d1.get_item_d(),'\t','\t', item_d1.get_unit_i(),'\t','\t', item_d1.get_price_r(), sep = ' ')
    print(item_d2.get_item_d(),'\t', item_d2.get_unit_i(),'\t','\t', item_d2.get_price_r(), sep = ' ')
    print(item_d3.get_item_d(),'\t','\t', item_d3.get_unit_i(),'\t','\t', item_d3.get_price_r(), sep = ' ')

main()

    

    
      



