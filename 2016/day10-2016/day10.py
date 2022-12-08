with open('input_day10.txt', 'r') as f:
    lines = f.readlines()


bots = [[] for _ in range(256)]
outputs = [None] * 24
bot_links = [[None, None] for _ in range(256)]

for line in lines:
    words = line.split()
    if words[0] == 'value':
        bots[int(words[-1])].append(int(words[1]))
        continue
    if words[0] == 'bot':
        number = int(words[1])
        low = int(words[6])
        if words[5] == 'output':
            low += 1000
        high = int(words[11])
        if words[10] == 'output':
            high += 1000
        bot_links[number] = [low, high]

while True:
    i = 0
    for i in range(len(bots)):
        if len(bots[i]) == 2:
            if 17 in bots[i] and 61 in bots[i]:
                print(i)
            break
    else:
        break
    if bot_links[i][0] < 1000:
        bots[bot_links[i][0]].append(min(bots[i]))
    else:
        outputs[bot_links[i][0] - 1000] = min(bots[i])
    if bot_links[i][1] < 1000:
        bots[bot_links[i][1]].append(max(bots[i]))
    else:
        outputs[bot_links[i][1] - 1000] = max(bots[i])
    bots[i] = []

print(outputs[0] * outputs[1] * outputs[2])
