TEST = False
filename = 'test-2025-11.txt' if TEST else 'input-2025-11.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children


nodes = {}
for line in lines:
    name, children = line.strip().split(':')
    children =  children.strip().split(' ')
    nodes[name] = children

cache = {}
def ways_to_out(node):
    if node in cache:
        return cache[node]
    ways = 0
    with_fft = 0
    with_dac = 0
    with_fft_and_dac = 0
    for child in nodes[node]:
        if child == 'out':
            ways += 1
        else:
            ch_ways, ch_with_fft, ch_with_dac, ch_with_fft_and_dac = ways_to_out(child)
            ways += ch_ways
            with_fft += ch_with_fft
            with_dac += ch_with_dac
            with_fft_and_dac += ch_with_fft_and_dac
    if node == 'fft':
        with_fft = ways
        if with_dac > 0:
            with_fft_and_dac = with_dac
    if node == 'dac':
        with_dac = ways
        if with_fft > 0:
            with_fft_and_dac = with_fft
    cache[node] = (ways, with_fft, with_dac, with_fft_and_dac)
    return (ways, with_fft, with_dac, with_fft_and_dac)


print(ways_to_out('svr'))
    