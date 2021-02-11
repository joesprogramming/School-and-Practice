#Joe Joseph

# Paint Job Estimator

# Hours of labor

def main(sft):
    value = sft / 112 * 8
    return value

# Gallons of paint

def gallons(gal):
    paint = gal / 112
    return paint

# Cost of paint

def paint_cost(pc, n):
    cost = n / 112 * pc
    return cost

# Labor Cost

def labor_cost(lc):
    laborCost = lc / 112 * 35 * 8
    return laborCost

# Total Cost of job

def total_cost(tc, gal):
    totalCost = tc / 112 * 35 * 8
    return totalCost

# defind called variables

f = float(input('Enter the square feet of wall to be paint: ' ,))
g = float(input('How much does a gallon of paint cost: $ ' ,))

# Call functions

labor = main(f)
paint_gallons = gallons(f)
pc = paint_cost(f, g)
lc = labor_cost(f)
tc = total_cost(f, g) + paint_cost(f, g)

# Print totals

print('Gallons of paint: ' , paint_gallons)
print('Hours of labor: ' , labor)
print('Cost of the Paint: $', pc)
print('Labor cost: $', lc)
print('Total cost of the paint job: $', tc)
