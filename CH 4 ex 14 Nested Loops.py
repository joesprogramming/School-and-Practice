#Joe Joseph
# Intro to programming

#Print a patteren with a nested loop

# number of rows
base = 7

# Loop to build upside down pyramid

for r in range(base):
    for c in range(7 - r):
        print('*', end='')
    print()
