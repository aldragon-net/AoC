TEST = False
filename = 'test-2025-05.txt' if TEST else 'input-2025-05.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

fresh_ranges = []
ids = []
for line in lines:
    if line.strip() == '':
        continue
    if '-' in line:
        fresh_ranges.append((int(line.strip().split('-')[0]), int(line.strip().split('-')[1])))
        continue
    ids.append(int(line.strip()))

fresh_count = 0

for id in ids:
    fresh = False
    for fresh_range in fresh_ranges:
        if fresh_range[0] <= id <= fresh_range[1]:
            fresh = True
            break
    if fresh:
        fresh_count += 1
        continue

print(fresh_count)

true_ranges = []

while fresh_ranges:
    the_range = fresh_ranges.pop()
    merged = False
    for i in range(len(fresh_ranges)):
        if not (fresh_ranges[i][1] < the_range[0]-1 or fresh_ranges[i][0] > the_range[1]+1):
            fresh_ranges[i] = (min(fresh_ranges[i][0], the_range[0]), max(fresh_ranges[i][1], the_range[1]))
            merged = True
    if not merged:
        true_ranges.append(the_range)

total = 0
for r in true_ranges:
    total += (r[1] - r[0] + 1)

print(total)
