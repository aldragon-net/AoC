passs = []
with open('day02input.txt') as inpfile:
    while True:
        st = inpfile.readline()
        if st == '':
            break
        st = st.strip()
        low, high, ch = int(st.split(':')[0].split(' ')[0].split('-')[0]), \
                        int(st.split(':')[0].split(' ')[0].split('-')[1]), \
                        st.split(':')[0].split(' ')[1]
        password = st.split(':')[1].strip()
        passs.append((low, high, ch, password))

# part one
n_valid = 0
for p in passs:
    low, high, ch, password = p
    n_in = password.count(ch)
    if low <= n_in <= high:
        n_valid += 1
print('part 1: there are {} valid passwords'.format(n_valid))

# part two
n_valid = 0
for p in passs:
    pos1, pos2, ch, password = p
    pos1 -= 1
    pos2 -= 1
    is1 = password[pos1] == ch
    is2 = password[pos2] == ch
    if (is1 and not is2) or (is2 and not is1):
        n_valid += 1
print('part 2: there are {} valid passwords'.format(n_valid))
