with open('input_day01.txt', 'r') as f:
    lines = f.readlines()
    f.close()

depths = [int(x.strip()) for x in lines]

# part 1
count = 0
prev = depths[0]
for depth in depths:
    if depth > prev:
        count += 1
    prev = depth
print(count)
# end of part 1

# part 2
count = 0
prev = sum(depths[:3])
for i in range(3, len(depths)+1):
    newsum = sum(depths[i-3:i])
    if newsum > prev:
        count += 1
    prev = newsum
print(count)
# end of part 2
