TEST = False

MAX = 9 if TEST else 4294967295
filename = 'test-2016-20.txt' if TEST else 'input-2016-20.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

blocked_regions = [tuple([int(value) for value in line.strip().split('-')]) for line in lines]

allowed = [(0, MAX)]


def block_allowed(allowed, block):
    a_start, a_end = allowed
    b_start, b_end = block
    if b_end < a_start or b_start > a_end:
        return [allowed]
    if b_start <= a_start and b_end >= a_end:
        return []
    if b_start <= a_start and a_start <= b_end < a_end:
        return [(b_end+1, a_end)]
    if a_start < b_start <= a_end and b_end >= a_end:
        return [(a_start, b_start-1)]
    return [(a_start, b_start-1), ((b_end+1, a_end))]


for blocked_region in blocked_regions:
    new_allowed = []
    for allowed_region in allowed:
        new_allowed.extend(block_allowed(allowed_region, blocked_region))
    allowed = new_allowed

print('part 1, lowest allowed IP:', allowed[0][0])

allowed_count = 0
for allowed_region in allowed:
    a_start, a_end = allowed_region
    allowed_count += a_end - a_start + 1

print('part 2, IPs allowed:', allowed_count)
