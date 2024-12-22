from functools import lru_cache
import itertools


TEST = False
filename = 'test-2024-21.txt' if TEST else 'input-2024-21.txt'
with open(filename, 'r') as f:
    codes = [line.strip() for line in f.readlines()]

numeric_layout = {
    'A': (2, 0),
    '0': (1, 0),
    '1': (0, 1),
    '2': (1, 1),
    '3': (2, 1),
    '4': (0, 2),
    '5': (1, 2),
    '6': (2, 2),
    '7': (0, 3),
    '8': (1, 3),
    '9': (2, 3)
}

directional_layout = {
    'A': (2, 1),
    '<': (0, 0),
    'v': (1, 0),
    '>': (2, 0),
    '^': (1, 1)
}

dx_sym = {
    1: '>',
    0: '',
    -1: '<'
}
dy_sym = {
    1: '^',
    0: '',
    -1: 'v'
}

directions = {
    '<': (-1, 0),
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    'A': (0, 0)
}


@lru_cache(maxsize=None)
def all_routes(shift):
    x, y = shift
    dx = x//abs(x) if x != 0 else 0
    dy = y//abs(y) if y != 0 else 0
    line = dx_sym[dx]*abs(x) + dy_sym[dy]*abs(y)
    return [''.join(x) + 'A' for x in set(itertools.permutations(line))]


@lru_cache(maxsize=None)
def route_is_valid(seq, start_pos, gap_pos):
    x, y = start_pos
    for sym in seq:
        dx, dy = directions[sym]
        x, y = x + dx, y + dy
        if (x, y) == gap_pos:
            return False
    return True


@lru_cache(maxsize=None)
def valid_routes(start_pos, end_pos, gap_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    delta_x, delta_y = end_x - start_x, end_y - start_y
    routes = all_routes((delta_x, delta_y))
    valid_routes = []
    for route in routes:
        if route_is_valid(route, start_pos, gap_pos):
            valid_routes.append(route)
    return valid_routes


@lru_cache(maxsize=None)
def sequence(input, mode='DIRECTIONAL'):
    if mode == 'NUMERICAL':
        gap_pos = (0, 0)
        x, y = (2, 0)
    if mode == 'DIRECTIONAL':
        gap_pos = (0, 1)
        x, y = (2, 1)
    variants = []
    for sym in input:
        sym_position = numeric_layout[sym] if mode == 'NUMERICAL' else directional_layout[sym]
        sym_x, sym_y = sym_position
        variants.append(valid_routes((x, y), (sym_x, sym_y), gap_pos))
        x, y = sym_x, sym_y
    return [''.join(x) for x in list(itertools.product(*variants))]


@lru_cache(maxsize=None)
def count(seq, depth):
    if depth == 0:
        return len(seq)
    length = 0
    for subseq in seq.split('A')[:-1]:
        routes = sequence(subseq+'A')
        length += min([count(s, depth-1) for s in routes])
    return length


sum = 0
for code in codes:
    code_value = int(code[:3])
    num_seqs = sequence(code, mode='NUMERICAL')
    length = min([count(seq, 25) for seq in num_seqs])
    sum += code_value * length

print(sum)
