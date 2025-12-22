TEST = False
filename = 'test-2018-07.txt' if TEST else 'input-2018-07.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

allowed_by = {}
requires = {}
for line in lines:
    words = line.strip().split(' ')
    prev, next = words[1], words[-3]
    if prev not in allowed_by:
        allowed_by[prev] = [next]
    else:
        allowed_by[prev].append(next)
    if next not in requires:
        requires[next] = [prev]
    else:
        requires[next].append(prev)

for req in requires:
    if req not in allowed_by:
        allowed_by[req] = []


# part 1
# steps_done = []
# while allowed_by:
#     available_steps = []
#     for step in allowed_by:
#         if step not in requires:
#             available_steps.append(step)
#     available_steps.sort()
#     step_done = available_steps[0]
#     steps_done.append(step_done)
#     del allowed_by[step_done]
#     to_delete = []
#     for step, requirements in requires.items():
#         if step_done in requirements:
#             requirements.remove(step_done)
#         if not requirements:
#             to_delete.append(step)
#     for step in to_delete:
#         del requires[step]
# print(''.join(steps_done))

# part 2
