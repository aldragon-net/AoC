with open('input_day10.txt', 'r') as f:
    lines = f.readlines()


bots = [[] for _ in range(256)]
outputs = [None] * 20
bot_links = [[None, None] for _ in range(256)]

for line in lines:
    words = line.split()
    if words[0] == 'value':
        bots[int(words[-1])].append(int(words[1]))
        continue
    if words[0] == 'bot':
        pass
