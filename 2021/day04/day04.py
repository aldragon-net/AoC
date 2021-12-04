with open('input_day04.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    f.close()

inputs = [int(x) for x in lines[0].split(',')]

boards = []

i = 2
while True:
    board = []
    for j in range(5):
        board.append([int(x) for x in lines[i].split()])
        i += 1
    boards.append(board)
    i += 1
    if i > len(lines)-1:
        break


def check_win(board):
    win = False
    for i in range(5):
        if (not any([x > 0 for x in board[i]])) or (
            not any([x > 0 for x in [board[0][i], board[1][i], board[2][i],
                     board[3][i], board[4][i]]])):
            win = True
    return win


def boardsum(board):
    s = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == -1:
                pass
            else:
                s += board[i][j]
    return s


winboards = []

for number in inputs:
    print(number)
    for b in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[b][i][j] == number:
                    boards[b][i][j] = -1
    for b in range(len(boards)):
        if b in winboards:
            continue
        if check_win(boards[b]):
            print('Win!', b, number, boardsum(boards[b])*number)
            winboards.append(b)
