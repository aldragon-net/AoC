from collections import Counter

with open('input_day04-2018.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

lines.sort()

guards = {}

guard_number = None
sleep_start = 0
sleep_end = 0

for line in lines:
    minutes = int(line.split(']')[0].split(':')[1])
    if line.split(']')[1].split()[0] == 'Guard':
        guard_number = line.split(']')[1].split()[1]
        if guard_number not in guards:
            guards[guard_number] = []
    elif line.split(']')[1].split()[0] == 'falls':
        sleep_start = minutes
    elif line.split(']')[1].split()[0] == 'wakes':
        sleep_end = minutes
        guards[guard_number].extend([t for t in range(sleep_start, sleep_end)])

max_sleep = 0
for guard in guards:
    if len(guards[guard]) > max_sleep:
        max_sleep = len(guards[guard])
        sleepest = guard

print(sleepest, max_sleep)

counter = Counter(guards[sleepest])

print(counter.most_common(1))

max_per_minute = 0
for guard in guards:
    if not guards[guard]:
        continue
    counter = Counter(guards[guard])
    print(counter.most_common(1))
    if counter.most_common(1)[0][1] > max_per_minute:
        max_per_minute = counter.most_common(1)[0][1]
        sleep_minute = counter.most_common(1)[0][0]
        sleepest = guard

print(sleepest, max_per_minute, sleep_minute)


