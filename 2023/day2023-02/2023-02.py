with open('input-2023-02.txt', 'r') as f:
    lines = f.readlines()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

games = []
for line in lines:
    line = line.split(': ')[1]
    game = []
    rounds = line.split('; ')
    for round in rounds:
        result = [0, 0, 0]
        colors = round.split(', ')
        for color in colors:
            value = int(color.split()[0])
            colorname = color.split()[1]
            if colorname == 'red':
                result[0] = value
            elif colorname == 'green':
                result[1] = value
            elif colorname == 'blue':
                result[2] = value
        game.append(result)
    games.append(game)

ids_sum = 0
power_sum = 0
for id0, game in enumerate(games):
    max_red = max([round[0] for round in game])
    max_green = max([round[1] for round in game])
    max_blue = max([round[2] for round in game])
    power = max_red * max_green * max_blue
    power_sum += power
    if any([max_red > RED_MAX, max_green > GREEN_MAX, max_blue > BLUE_MAX]):
        continue
    ids_sum += (id0 + 1)

print(ids_sum)
print(power_sum)
