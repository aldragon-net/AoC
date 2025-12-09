TEST = False
filename = 'test-2025-02.txt' if TEST else 'input-2025-02.txt'
with open(filename, 'r') as f:
    lines = f.readlines()


def is_invalid_p1(id):
    id = str(id)
    if len(id) % 2 != 0:
        return False
    half = len(id) // 2
    if id[:half] == id[half:]:
        return True
    return False


def is_invalid_p2(id):
    id = str(id)
    length = len(id)
    if length == 1:
        return False
    dividers = [len(id)]
    for i in range(2, length // 2 + 1):
        if length % i == 0:
            dividers.append(i)
    for divider in dividers:
        part_length = length // divider
        unique_parts = set()
        for i in range(divider):
            unique_parts.add(id[part_length*i:part_length*(i+1)])
        if len(unique_parts) == 1:
            return True
    return False


str_ranges = lines[0].strip().split(',')
int_ranges = []
for str_range in str_ranges:
    a, b = str_range.split('-')
    int_ranges.append((int(a), int(b)))

invalid_sum_p1 = 0
invalid_sum_p2 = 0
for int_range in int_ranges:
    for id in range(int_range[0], int_range[1]+1):
        if is_invalid_p1(id):
            invalid_sum_p1 += id
        if is_invalid_p2(id):
            invalid_sum_p2 += id

print(invalid_sum_p1)
print(invalid_sum_p2)
