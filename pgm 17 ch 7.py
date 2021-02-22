# Joe Joseph
# Intro to Programming

# Total Sales


user = int(input('Enter the total number of days you wish to calculate the sales for: ' ,))

num_days = user


def main():
    #create list
    sales = [0] * num_days

    #variable to hold index

    index = 0

    print('Enter sales for the day')

    #Get Sales
    while index < num_days:
        print('Day # ' , index + 1 , ':', sep='', end='')
        sales[index] = float(input())
        index += 1


    print('Sales for the day' )
    for value in sales:
        print('Total sales today were: $ ', value)
    print('The total earnings this week are: $', sum(sales))


main()

