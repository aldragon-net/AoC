with open('input_day02.txt', 'r') as f:
    lines = f.readlines()

results_p1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

results_p2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

sum_1 = 0
sum_2 = 0

for line in lines:
    sum_1 += results_p1[line.strip()]
    sum_2 += results_p2[line.strip()]

print(sum_1)
print(sum_2)
