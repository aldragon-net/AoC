with open('input_day07.txt', 'r') as f:
    line = f.readline().strip()
    f.close()

crabs = [int(x) for x in line.split(',')]

fuel_spent = {}
f = 0
for i in range(2000):
    fuel_spent[i] = f
    f = f + (i+1)

min_fuel = 99999999
for mean_pos in range(2000):
    fuel = 0
    for crab in crabs:
        # fuel += abs(crab-mean_pos)                # part 1
        fuel += fuel_spent[abs(crab-mean_pos)]    # part 2
    if fuel < min_fuel:
        min_fuel = fuel
print(min_fuel)
