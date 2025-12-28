states = {}
initial_state = (1, 1, 1, 3, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 1)
desired_state = (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
paths = {initial_state: 0}


def is_valid(state):
    for i in range(len(state)):
        if state[i] < 1 or state[i] > 4:
            return False
    for e in [1, 3, 5, 7, 9, 11, 13]:
        chip_floor = state[e]
        gen_floor = state[e+1]
        if chip_floor == gen_floor:
            continue
        for other_e in [1, 3, 5, 7, 9, 11, 13]:
            if e == other_e:
                continue
            other_gen_floor = state[other_e+1]
            if chip_floor == other_gen_floor:
                return False
    return True


def get_new_states(state):

    def add_state_if_valid(statelist):
        state = tuple(statelist)
        if is_valid(state):
            new_states.add(state)

    el_floor = state[0]
    same_floor_items = []
    new_states = set()
    for i in range(1, len(state)):
        if state[i] == el_floor:
            same_floor_items.append(i)
    for i in same_floor_items:
        new_state_up = list(state)
        new_state_up[0], new_state_up[i] = new_state_up[0]+1, new_state_up[i]+1
        add_state_if_valid(new_state_up)
        new_state_down = list(state)
        new_state_down[0], new_state_down[i] = new_state_down[0]-1, new_state_down[i]-1
        add_state_if_valid(new_state_down)
        for j in same_floor_items:
            if j == i:
                continue
            new_state_up = list(state)
            new_state_up[0], new_state_up[i], new_state_up[j] = (
                new_state_up[0]+1, new_state_up[i]+1, new_state_up[j]+1
            )
            add_state_if_valid(new_state_up)
            new_state_down = list(state)
            new_state_down[0], new_state_down[i], new_state_down[j] = (
                new_state_down[0]-1, new_state_down[i]-1, new_state_down[j]-1
            )
            add_state_if_valid(new_state_down)
    return new_states


front = [initial_state]
move = 0
while front:
    move += 1
    new_states = set()
    new_front = set()
    for state in front:
        new_states.update(get_new_states(state))
    for new_state in new_states:
        if new_state not in paths:
            new_front.add(new_state)
            paths[new_state] = move
    front = new_front
    if desired_state in paths:
        break

print(paths[desired_state])
