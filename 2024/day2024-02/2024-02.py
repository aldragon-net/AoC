TEST = False

if TEST:
    filename = 'test-2024-02.txt'
else:
    filename = 'input-2024-02.txt'

with open(filename, 'r') as f:
    lines = f.readlines()


reports = []
for line in lines:
    reports.append([int(x) for x in line.strip().split()])


def isrepsafe(report):
    safe = True
    if report[0] == report[-1]:
        return False
    if report[-1] > report[0]:
        ascending = True
    else:
        ascending = False
    for i in range(1, len(report)):
        if ascending and (report[i] > report[i-1] and report[i] <= report[i-1] + 3):
            continue
        if not ascending and (report[i] < report[i-1] and report[i] >= report[i-1] - 3):
            continue
        safe = False
    return safe


safecount = 0
for report in reports:
    if isrepsafe(report):
        safecount += 1
print(safecount)

safecount = 0
for report in reports:
    if isrepsafe(report):
        safecount += 1
        continue
    else:
        for i in range(len(report)):
            repcopy = []
            for j in range(len(report)):
                if j == i:
                    continue
                repcopy.append(report[j])
            if isrepsafe(repcopy):
                safecount += 1
                break

print(safecount)