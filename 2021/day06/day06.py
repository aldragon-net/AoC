with open('input_day06.txt', 'r') as f:
    line = f.readline().strip()
    f.close()


fish = [int(x) for x in line.split(',')]

fish = [1]

day = 0
# naive part 1
while day < 80:
    day += 1
    newcount = 0
    for i in range(len(fish)):
        if fish[i] == 0:
            newcount += 1
            fish[i] = 6
        else:
            fish[i] -= 1
    for i in range(newcount):
        fish.append(8)

print(len(fish))

# part 2
fish = [int(x) for x in line.split(',')]

database = {}


def calc_off_base(days):
    if days in database.keys():
        return database[days]
    else:
        day = 0
        fish = 8
        offspring = 1
        while day < days:
            day += 1
            if fish == 0:
                fish = 6
                offspring += calc_off_base(days - day)
            else:
                fish -= 1
        database[days] = offspring
        return offspring


for i in range(264):
    n = calc_off_base(i)


total_offspring = 0
for f in fish:
    total_offspring += database[256+(8-f)]

print(total_offspring)
