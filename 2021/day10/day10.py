with open('input_day10.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()


point = {')': 3,
         ']': 57,
         '}': 1197,
         '>': 25137,
         '(': -3,
         '[': -57,
         '{': -1197,
         '<': -25137
         }

scorepoint = {'(': 1,
              '[': 2,
              '{': 3,
              '<': 4,
              }


def checkline(line):
    stack = []
    for i in range(len(line)):
        char = line[i]
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        if char in [')', ']', '}', '>']:
            match = stack.pop()
            if point[char] + point[match] != 0:
                return point[char]
    return 0


def line_score(line):
    stack = []
    for i in range(len(line)):
        char = line[i]
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        if char in [')', ']', '}', '>']:
            stack.pop()
    score = 0
    while len(stack) > 0:
        score *= 5
        char = stack.pop()
        score += scorepoint[char]
    return score


total = 0
incomplete = []

for line in lines:
    score = checkline(line)
    if score == 0:
        incomplete.append(line)
    else:
        total += checkline(line)
print(total)

scores = [line_score(line) for line in incomplete]
scores.sort()

print(scores[len(scores)//2])
