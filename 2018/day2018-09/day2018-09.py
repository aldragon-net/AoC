PLAYERS = 416
LAST = 7197500

circle = [0]
position = 0
marble = 1

scores = [0 for i in range(PLAYERS)]
player = 0


class Marble:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


seed = Marble(0, None, None)
seed.left = seed
seed.right = seed
position = seed

while marble <= LAST:
    if marble % 23 == 0:
        position = position.left.left.left.left.left.left
        left = position.left
        right = position.right
        removed = position.value
        scores[player] += marble + removed
        left.right, right.left = right, left
    else:
        position = position.right.right
        next = position.right
        new = Marble(marble, position, next)
        position.right = new
        next.left = new
    player = (player + 1) % PLAYERS
    marble += 1

scores.sort(reverse=True)
print(scores[0])
