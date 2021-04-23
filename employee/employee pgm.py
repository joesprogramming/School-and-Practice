# Joe Joseph

#Intro to Programming

#Ch. 11


import employee



def main():

    worker = input('Enter workers shift number(1 or 2): ')

    s = worker

    rate = input('Enter the workers hourly pay rate: $ ')

    cd = employee.production_worker(worker, rate)

    cd.day_shift()

    print('Pay', cd.get_pay())


main()
