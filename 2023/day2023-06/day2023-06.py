TEST = False
filename = 'test-2023-06.txt' if TEST else 'input-2023-06.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

times = [int(i) for i in lines[0].strip().split(':')[1].split()]
records = [int(i) for i in lines[1].strip().split(':')[1].split()]


def investigate_race(time, record):
    count = 0
    for t_press in range(time):
        velocity = t_press
        remaining_time = time - t_press
        distance = velocity * remaining_time
        if distance > record:
            count += 1
    return count


result = 1
for i in range(len(times)):
    time = times[i]
    record = records[i]
    result = result * investigate_race(time, record)

print(result)
