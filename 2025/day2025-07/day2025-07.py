import re

TEST = False
filename = 'test-2025-07.txt' if TEST else 'input-2025-07.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

beams = set()
beams.add(lines[0].find('S'))

split_count = 0
for i in range(1, len(lines)):
    line = lines[i].strip()
    splitters = [s.start() for s in re.finditer(r'\^', line)]
    for splitter in splitters:
        if splitter in beams:
            beams.remove(splitter)
            beams.add(splitter+1)
            beams.add(splitter-1)
            split_count += 1

print(split_count)

cached = {}


def timelines(beam, i_line):
    if (beam, i_line) in cached:
        return cached[(beam, i_line)]
    if i_line == len(lines)-1:
        cached[(beam, i_line)] = 1
        return 1
    splitters = [s.start() for s in re.finditer(r'\^', lines[i_line].strip())]
    if beam not in splitters:
        cached[(beam, i_line)] = timelines(beam, i_line+1)
    else:
        cached[(beam, i_line)] = timelines(beam+1, i_line+1) + timelines(beam-1, i_line+1)
    return cached[(beam, i_line)]


beam = lines[0].find('S')
print(timelines(beam, 0))
