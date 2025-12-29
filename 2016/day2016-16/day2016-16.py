TEST = False

SEED = '10000' if TEST else '11110010111001001'
DISK_LENGTH = 20 if TEST else 35651584  # 272 for part 1


def fill_disk(length, seed):
    while len(seed) < length:
        flipped = []
        for i in range(len(seed)):
            next = '0' if seed[i] == '1' else '1'
            flipped.append(next)
        flipped = ''.join(flipped[::-1])
        seed = seed + '0' + flipped
    return seed[:length]


def find_checksum(disk):
    while len(disk) % 2 == 0:
        hash = []
        for i in range(len(disk)//2):
            if disk[i*2] == disk[i*2+1]:
                hash.append('1')
            else:
                hash.append('0')
        disk = hash
    return ''.join(hash)


disk = fill_disk(DISK_LENGTH, SEED)
print(find_checksum(disk))
