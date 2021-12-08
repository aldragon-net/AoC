with open('input_day08.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

# part 1

count = 0
for line in lines:
    output = line.split('|')[1].strip()
    signals = output.split()
    for signal in signals:
        if len(signal) in [2, 3, 4, 7]:
            count += 1

print(count)

# part 2

digits = {0: 'abcefg',
          1: 'cf',
          2: 'acdeg',
          3: 'acdfg',
          4: 'bcdf',
          5: 'abdfg',
          6: 'abdefg',
          7: 'acf',
          8: 'abcdefg',
          9: 'abcdfg'
          }

let_counts = {}
for digit, lets in digits.items():
    for char in lets:
        if char not in let_counts.keys():
            let_counts[char] = 1
        else:
            let_counts[char] += 1

print(let_counts)

decoder = {}
for i, digit in digits.items():
    s = ''
    for char in digit:
        s += str(let_counts[char])
    s = ''.join(sorted(s))
    decoder[s] = i

print(decoder)

sum = 0
numbers = []

for line in lines:
    codigits = line.split('|')[0].strip()
    let_counts = {}
    for char in 'abcdefg':
        let_counts[char] = codigits.count(char)
    
    number = []
    output = line.split('|')[1].strip().split()
    for digit in output:
        s = ''
        for char in digit:
            s += str(let_counts[char])
            s = ''.join(sorted(s))
        number.append(decoder[s])
    numbers.append(number)

sum = 0
for number in numbers:
    dignum = [str(x) for x in number]
    num = int(''.join(dignum))
    sum += num
print(sum)
        