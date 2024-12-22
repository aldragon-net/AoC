TEST = False
filename = 'test-2024-22.txt' if TEST else 'input-2024-22.txt'
with open(filename, 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]


def generate(number):
    x = number * 64
    number = x ^ number
    number = number % 16777216
    x = number // 32
    number = x ^ number
    number = number % 16777216
    x = number * 2048
    number = x ^ number
    number = number % 16777216
    return number


def generate_nth(number, n):
    i = 0
    while i < n:
        number = generate(number)
        i += 1
    return number

# part 1
# sum = 0
# for number in numbers:
#     number = generate_nth(number, 2000)
#     sum += number
# print(sum)


def generate_sequences(number, n):
    seq2price = {}
    price = number % 10
    deltas = []
    for i in range(n):
        new_number = generate(number)
        new_price = new_number % 10
        delta = new_price - price
        deltas.append(delta)
        if i >= 3:
            sequence = tuple(deltas[-4:])
            if sequence not in seq2price:
                seq2price[sequence] = new_price
        number = new_number
        price = new_price
    return seq2price


all_seqs = set()
seq2prices = []
for number in numbers:
    seq2price = generate_sequences(number, 2000)
    seq2prices.append(seq2price)
    all_seqs.update(seq2price.keys())

max_bananas = 0
for seq in all_seqs:
    sum = 0
    for seq2price in seq2prices:
        if seq in seq2price:
            sum += seq2price[seq]
    if sum > max_bananas:
        max_bananas = sum

print(max_bananas)
