lines = []
with open('day04input.txt', 'r') as inpfile:
    while True:
        line = inpfile.readline().strip()
        if line == '':
            break
        lines.append(line)

idsum = 0

ABC = 'abcdefghijklmnopqrstuvwxyz'
        
for line in lines:
    print(line)
    checksum = line.split('[')[1].strip(']')
    id = int(line.split('[')[0].split('-')[-1])
    letters = ''.join(line.split('[')[0].split('-')[:-1])
    valid = True
    letcount = [letters.count(char) for char in ABC]
    letcount.sort(reverse = True)
    checkcount = [letters.count(char) for char in checksum]
    print(letcount)
    print(checkcount)
    if letcount[:5] == checkcount:
        print('Valid!')
        idsum = idsum + id
    shift = id % 26
    decoded_letters = []
    for char in letters:
        decoded_letters.append(ABC[((ABC.find(char) + shift) % 26)])
    decoded = ''.join(decoded_letters)
    print(decoded)
    if decoded[0:5] == 'north':
        print('FOUND IT! id is', id)
        input()

print('Sum of valid room\'s ids is:', idsum)


input()


