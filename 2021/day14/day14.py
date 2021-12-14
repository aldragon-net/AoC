with open('input_day14.txt', 'r') as f:
    polymer = f.readline().strip()
    line = f.readline()
    line = f.readline()
    rules = {}
    while line != '':
        pair, insertion = line.strip().split(' -> ')
        rules[pair] = insertion
        line = f.readline()
    f.close()

# # naive solution for part 1
#
# def generate_polymer(polymer):
#     new_pol = []
#     for i in range(len(polymer)):
#         if i == len(polymer):
#             new_pol.append(polymer[i])
#         else:
#             insertion = rules.get(polymer[i:i+2], '')
#             new_pol.extend([polymer[i], insertion])
#     new_pol = ''.join(new_pol)
#     return new_pol
#
# for i in range(10):
#     polymer = generate_polymer(polymer)
#

alphabet = ['B', 'C', 'F', 'H', 'K', 'N', 'O', 'S', 'P', 'V']

call_rules = {}
for pair, insertion in rules.items():
    new_pair_1 = ''.join([pair[0], insertion])
    new_pair_2 = ''.join([insertion, pair[1]])
    call_rules[pair] = (new_pair_1, new_pair_2)

add_rules = {}
for pair, insertion in rules.items():
    add_rules[pair] = {}
    add_rules[pair][0] = [0 for i in range(10)]
    add_list = [0 for i in range(10)]
    add_list[alphabet.index(insertion)] = 1
    add_rules[pair][1] = add_list

def get_add(pair, n):
    if n in add_rules[pair].keys():
        return add_rules[pair][n]
    else:
        insertion = rules[pair]
        pair1, pair2 = call_rules[pair]      
        add_1 = get_add(pair1, n-1)
        add_2 = get_add(pair2, n-1)
        new = [sum(i) for i in zip(add_1, add_2)]
        new[alphabet.index(insertion)] += 1
        add_rules[pair][n] = new
        return new

def get_answer(N):
    total_count = [0 for i in range(10)]
    for i in range(10):
        total_count[i] = polymer.count(alphabet[i])
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        pair_count = get_add(pair, N)
        total_count = [sum(i) for i in zip(total_count, pair_count)]
    return max(total_count)-min(total_count)

print('part 1:', get_answer(10))
print('part 2:', get_answer(40))
