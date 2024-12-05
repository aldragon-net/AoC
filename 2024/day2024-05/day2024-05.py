TEST = False
filename = 'test-2024-05.txt' if TEST else 'input-2024-05.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

rules = []
books = []
for line in lines:
    if '|' in line:
        page1, page2 = [int(x) for x in line.strip().split('|')]
        rules.append((page1, page2))
    if ',' in line:
        books.append(([int(x) for x in line.strip().split(',')]))

midsum = 0
corsum = 0

for book in books:
    is_correct = True
    for rule in rules:
        x1, x2 = rule
        if x1 in book and x2 in book:
            if book.index(x1) > book.index(x2):
                is_correct = False
                break
    if is_correct:
        midsum += book[(len(book)-1)//2]
    else:
        edited = book.copy()
        while not is_correct:
            is_correct = True
            for rule in rules:
                x1, x2 = rule
                if x1 in edited and x2 in edited:
                    i1, i2 = edited.index(x1), edited.index(x2)
                    if i1 > i2:
                        is_correct = False
                        edited[i1], edited[i2] = edited[i2], edited[i1]
                        break
        corsum += edited[(len(edited)-1)//2]

print(midsum)
print(corsum)
