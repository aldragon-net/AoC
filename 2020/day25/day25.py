subj_number = 7
div_value = 20201227

with open('day25input.txt', 'r') as inpfile:
    key_door, key_card = [int(line.strip()) for line in inpfile.readlines()]

def loopit(value, subj_number):
    value = value * subj_number
    value = value % div_value
    return value

def loopn(subj_number, n):
    value = 1
    for i in range(n):
        value = loopit(value, subj_number)
    return value

n_loops = 0
found_door = False
found_card = False
pubkey = 1
while True:
    n_loops += 1
    pubkey = loopit(pubkey, subj_number)
    if pubkey == key_door:
        n_door = n_loops
        print('Door loops:', n_door)
        found_door = True
    elif pubkey == key_card:
        n_card = n_loops
        print('Card loops:', n_card)
        found_card = True
    if found_door and found_card:
        break

print('Encripton key is:', loopn(key_door, n_card))
print('Check:',  loopn(key_card, n_door))
