TEST = False
filename = 'test-2016-18.txt' if TEST else 'input-2016-18.txt'
with open(filename, 'r') as f:
    row = '#' + f.readline().strip() + '#'

ROWS = 400000


def generate_next_row(row):
    next_row = ['.' for char in row]
    next_row[0] = '#'
    next_row[-1] = '#'
    for i in range(1, len(row)-1):
        if (row[i-1] == '^' and row[i+1] != '^') or (row[i-1] != '^' and row[i+1] == '^'):
            next_row[i] = '^'
    return ''.join(next_row)


n_rows = 1
safe_count = row.count('.')
while n_rows < ROWS:
    row = generate_next_row(row)
    n_rows += 1
    safe_count += row.count('.')

print(safe_count)
