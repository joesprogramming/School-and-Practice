# Joe Joseph

#Intro to Programming

#Ch. 11


import person


#Call Function

def main():


    #Assign Variables. 

    name = person.Person('Frank', 'Citrus Road Hot Town FL 65633', '222-222-2222')

    sub = input('Does this client want to join our mailing lis?(Enter: Y/N): ')

    number = 0
        
    num = number + 1

    print(name.get_name_p(), '\n', name.get_address_1(), '\n', name.get_phone_1())

#Call Subclass

    cd = person.Customer(num, sub)

#Call Boolean function

    cd.list_mail()
    
    print(cd.get_name())    

    

    


main()
