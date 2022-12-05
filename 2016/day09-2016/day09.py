with open('input_day09.txt', 'r') as f:
    line = f.readline()


def unpacked_length(s, recursive=True):
    pos = 0
    unpacked = 0
    while pos < len(s):
        if s[pos] == '(':
            shift = 0
            while s[pos+shift] != ')':
                shift += 1
            operator = s[pos+1:pos+shift]
            le, n = [int(x) for x in operator.split('x')]
            if recursive:
                unpacked += n * unpacked_length(s[pos+shift+1:pos+le+shift+1])
            else:
                unpacked += n * le
            pos = pos + shift + le + 1
        else:
            pos += 1
            unpacked += 1
    return unpacked


print('Part 1:', unpacked_length(line, recursive=False))
print('Part 2:', unpacked_length(line))
