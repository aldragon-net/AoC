import copy


with open('test.txt', 'r') as f:
# with open('input_day16-2022.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


class Valve():
    def __init__(self, name, flow, connected_to, connected_from) -> None:
        self.name = name
        self.flow = flow
        self.connected_to = connected_to
        self.connected_from = connected_from
        self.paths = {}


class Status():
    def __init__(self, released=-1, open=[]) -> None:
        self.released = released
        self.open = open


valves = []
for line in lines:
    name = line.split()[1]
    flow = int(line.split()[4].strip(';').strip('rate='))
    connected_to = [valve.strip(',') for valve in line.split()[9:]]
    valves.append(Valve(name, flow, connected_to, []))

valves = sorted(valves, key=lambda v: v.name)

for j, valve in enumerate(valves):
    valve.connected_from.append(j)
    for valve_to in valve.connected_to:
        for v in valves:
            if v.name == valve_to:
                v.connected_from.append(j)

for valve in valves:
    for v in valve.connected_from:
        valve.paths[v] = 1
    while len(valve.paths) < len(valves):
        for v in list(valve.paths.keys()):
            for new in valves[v].connected_from:
                if new not in valve.paths:
                    valve.paths[new] = valve.paths[v] + 1
                else:
                    valve.paths[new] = min(valve.paths[new],
                                           valve.paths[v] + 1)


for valve in valves:
    print(valve.name, valve.flow, valve.connected_to, valve.connected_from)

mysol = [[[Status() for _ in range(27)] for _ in valves] for _ in valves]


mysol[0][0][0].released = 0

for t in range(1, 27):
    for i in range(len(valves)):
        for e in range(len(valves)):

            myvalve = valves[i]
            elvalve = valves[e]

            for j in myvalve.paths:
                steps = myvalve.paths[j]
                if t - steps < 0:
                    continue
                if mysol[i][e][t].released < mysol[j][e][t-steps].released:
                    mysol[i][e][t].released = mysol[j][e][t-steps].released
                    mysol[i][e][t].open = copy.deepcopy(
                                            mysol[j][e][t-steps].open
                                            )
            for j in elvalve.paths:
                steps = elvalve.paths[j]
                if t - steps < 0:
                    continue
                if mysol[i][e][t].released < mysol[i][j][t-steps].released:
                    mysol[i][e][t].released = mysol[i][j][t-steps].released
                    mysol[i][e][t].open = copy.deepcopy(
                                            mysol[i][j][t-steps].open
                                            )
            for j in myvalve.paths:
                steps = myvalve.paths[j]
                if j != i:
                    steps += 1
                if t - steps < 0:
                    continue
                if (mysol[j][e][t-steps].released >= 0 and
                        i not in mysol[j][e][t-steps].open):
                    if mysol[i][e][t].released < (
                                mysol[j][e][t-steps].released +
                                myvalve.flow * (26 - t)
                            ):
                        mysol[i][e][t].released = (
                            mysol[j][e][t-steps].released +
                            myvalve.flow * (26 - t)
                        )
                        mysol[i][e][t].open = copy.deepcopy(
                            mysol[j][e][t-steps].open
                        )
                        mysol[i][e][t].open.append(i)
                        print('i open', i)

            for j in elvalve.paths:
                steps = elvalve.paths[j]
                if j != e:
                    steps += 1
                if t - steps < 0:
                    continue
                if (mysol[i][j][t-steps].released >= 0 and
                        e not in mysol[i][j][t-steps].open):
                    if mysol[i][e][t].released < (
                                mysol[i][j][t-steps].released +
                                myvalve.flow * (26 - t)
                            ):
                        mysol[i][e][t].released = (
                            mysol[i][j][t-steps].released +
                            myvalve.flow * (26 - t)
                        )
                        mysol[i][e][t].open = copy.deepcopy(
                            mysol[i][j][t-steps].open
                        )
                        mysol[i][e][t].open.append(e)
                        print('elephant opens', e)

max_pressure = 0
for i in range(len(valves)):
    for j in range(len(valves)):
        print(i, j, mysol[i][j][-1].released)
        if max_pressure < mysol[i][j][-1].released:
            max_pressure = mysol[i][j][-1].released

print(max_pressure)

# # # working part 1:
#
# mysol = [[Status() for _ in range(27)] for _ in valves]
# mysol[0][0].released = 0
# for t in range(1, 27):
#     for i in range(len(valves)):
#         valve = valves[i]
#         for j in valve.paths:
#             steps = valve.paths[j]
#             if t - steps < 0:
#                 continue
#             if mysol[i][t].released < mysol[j][t-steps].released:
#                 mysol[i][t].released = mysol[j][t-steps].released
#                 mysol[i][t].open = copy.deepcopy(mysol[j][t-steps].open)
#         for j in valve.paths:
#             steps = valve.paths[j]
#             if j != i:
#                 steps += 1
#             if t - steps < 0:
#                 continue
#             if (mysol[j][t-steps].released >= 0 and
#                     i not in mysol[j][t-steps].open):
#                 if mysol[i][t].released < (
#                             mysol[j][t-steps].released +
#                             valve.flow * (30 - t)
#                         ):
#                     mysol[i][t].released = (
#                         mysol[j][t-steps].released +
#                         valve.flow * (30 - t)
#                     )
#                     mysol[i][t].open = copy.deepcopy(
#                         mysol[j][t-steps].open
#                     )
#                     mysol[i][t].open.append(i)

#     print(t, [mysol[i][t].released for i in range(len(valves))])
