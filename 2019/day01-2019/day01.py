import math

masses = []

with open('day01input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        masses.append(int(line))    

total_mass_1 = 0
total_mass_2 = 0

for mass in masses:
    total_mass_1 = total_mass_1 + (math.floor(mass/3) - 2)
    while True:
        if mass <=6:
            break
        fuel = (math.floor(mass/3) - 2)
        total_mass_2 = total_mass_2 + fuel
        mass = fuel
       
print('Total mass is', total_mass_1)
print('Total mass for 2nd approach is', total_mass_2)
input()        
