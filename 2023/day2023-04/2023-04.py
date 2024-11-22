with open('input-2023-04.txt', 'r') as f:
    lines = f.readlines()

cards = []
for line in lines:
    numbers = line.strip().split(': ')[1]
    winning_numbers, numbers_have = numbers.split(' | ')
    winning_numbers = [int(number) for number in winning_numbers.split()]
    numbers_have = [int(number) for number in numbers_have.split()]
    cards.append((winning_numbers, numbers_have))

card_points = []
card_copies = []
for card in cards:
    points = 0
    copies = 0
    winning_numbers, numbers_have = card
    for number in numbers_have:
        if number in winning_numbers:
            points = points*2 if points else 1
            copies += 1
    card_points.append(points)
    card_copies.append(copies)

n_cards = [1] * len(card_copies)

for i in range(len(n_cards)):
    depth = card_copies[i]
    for j in range(1, depth+1):
        n_cards[i+j] = n_cards[i+j] + n_cards[i]

print(sum(n_cards))
