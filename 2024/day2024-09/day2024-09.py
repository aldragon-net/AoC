TEST = True
filename = 'test-2024-09.txt' if TEST else 'input-2024-09.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
    line = lines[0].strip()

# part 1
disk = []
for i in range(len(line)//2+1):
    file_length = int(line[i*2])
    try:
        empty_length = int(line[i*2+1])
    except IndexError:
        empty_length = 0
    for j in range(file_length):
        disk.append(i)
    for j in range(empty_length):
        disk.append('.')
full_size = len(disk)

empty_pos = 0
while True:
    try:
        empty_pos = disk.index('.', empty_pos)
    except ValueError:
        break
    to_move = '.'
    while to_move == '.':
        to_move = disk.pop()
    disk[empty_pos] = to_move


def checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        checksum += i * disk[i]
    return checksum

print(checksum(disk))

# part 2
files = []
empties = []
position = 0
for i in range(len(line)//2+1):
    file_length = int(line[i*2])
    try:
        empty_length = int(line[i*2+1])
    except IndexError:
        empty_length = 0
    files.append((position, file_length))
    position += file_length
    empties.append((position, empty_length))
    position += empty_length

for i in range(len(files)-1, 0, -1):
    file = files[i]
    file_pos, file_length = file
    for j, empty in enumerate(empties):
        empty_pos, empty_length = empty
        if empty_pos > file_pos:
            break
        if empty_length >= file_length:
            files[i] = (empty_pos, file_length)
            empties[j] = (empty_pos + file_length, empty_length - file_length)
            break

disk = ['.'] * full_size
for i in range(len(disk)):
    disk[i] = '.'
for i, file in enumerate(files):
    file_pos, file_length = file
    for j in range(file_length):
        disk[file_pos+j] = i

print(checksum(disk))
