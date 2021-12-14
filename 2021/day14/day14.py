from collections import Counter

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


def generate_polymer(polymer):
    new_pol = []
    for i in range(len(polymer)):
        if i == len(polymer):
            new_pol.append(polymer[i])
        else:
            insertion = rules.get(polymer[i:i+2], '')
            new_pol.extend([polymer[i], insertion])
    new_pol = ''.join(new_pol)
    return new_pol

predictions = {}
for pair, insertion in rules.items():
    predictions[pair] = {0: pair,
                         1: ''.join([pair[0], insertion, pair[1]])
                         }

def predict_insertion(pair, n):
    if pair not in predictions.keys():
        return ''
    if n not in predictions[pair].keys():
        previous = ''.join([pair[0], predict_insertion(pair, n-1), pair[1]])
        new_pol = generate_polymer(previous)
        predictions[pair][n] = new_pol
    return predictions[pair][n][1:-1]


test = 'HF'
for i in range(5):
    test = generate_polymer(test)

print(test)

# part 1
# for i in range(10):
#     print(i)
#     polymer = generate_polymer(polymer)
# print(Counter(polymer))