with open('day15input.txt', 'r') as inpfile:
    inpnumbers = [int(x) for x in inpfile.readline().strip().split(',')]

numbers = {}
turn = 0
for num in inpnumbers:
    turn += 1
    numbers[num] = turn

nextnum = 0
while True:
    turn += 1
    if turn == 2020:  # part 1
        print('2020th number is', nextnum)
    elif turn == 30000000:  # part 2
        print('30000000th number is', nextnum)
        break
    if nextnum not in numbers.keys():
        numbers[nextnum], nextnum = turn, 0
    else:
        numbers[nextnum], nextnum = turn, turn - numbers[nextnum]
