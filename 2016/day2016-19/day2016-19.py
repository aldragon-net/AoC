ELVES = 3014603


# part 1
ring = [i+1 for i in range(ELVES)]
ring[-1] = 0
elf = 0
while True:
    left_elf = ring[elf]
    if left_elf == elf:
        break
    ring[elf] = ring[left_elf]
    elf = ring[elf]
print(elf+1)

# part 2
ring = [i+1 for i in range(ELVES)]
ring[-1] = 0
prev_to_across = len(ring)//2 - 1
step = 'odd'
while True:
    across = ring[prev_to_across]
    if across == prev_to_across:
        break
    ring[prev_to_across] = ring[across]
    if step == 'odd':
        prev_to_across = ring[prev_to_across]
        step = 'even'
    else:
        step = 'odd'
    elf = ring[elf]

print(across+1)
