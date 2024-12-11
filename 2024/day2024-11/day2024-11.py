TEST = False
filename = 'test-2024-11.txt' if TEST else 'input-2024-11.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

stones = [int(x) for x in lines[0].split()]

# part 1 naive
blinks = 0
while True:
    blinks += 1
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
            continue
        new_stones.append(stone*2024)
    stones = new_stones
    if blinks == 25:
        break

print(len(stones))

# part 2 not naive
stones = [int(x) for x in lines[0].split()]
database = {}


def stones_in(stone, blinks):
    if blinks == 0:
        return 1
    if (stone, blinks) in database:
        return database[(stone, blinks)]
    if stone == 0:
        number = stones_in(1, blinks-1)
        database[(0, blinks)] = number
        return number
    if len(str(stone)) % 2 == 0:
        stone_1 = int(str(stone)[:len(str(stone))//2])
        stone_2 = int(str(stone)[len(str(stone))//2:])
        number = stones_in(stone_1, blinks-1) + stones_in(stone_2, blinks-1)
        database[(stone, blinks)] = number
        return number
    number = stones_in(stone*2024, blinks-1)
    database[(stone, blinks)] = number
    return number


sum_stones = 0
for stone in stones:
    sum_stones += stones_in(stone, 75)

print(sum_stones)
