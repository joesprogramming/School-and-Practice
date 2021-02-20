# Joe Joseph

# Intro to programming

#Calculate average of numbers in .txt file

#Open file and reads it. Input your own file name. 
infile = open('numbers.txt', 'r')

#Variable

num = 0
l = 0
#Loop to calculate average

for line in infile:
    int_numbers = int(line)
    num += int_numbers
    l = l + 1
num = num / l

infile.close

#Print average


print('This is the average of the numbers: ' , num)
