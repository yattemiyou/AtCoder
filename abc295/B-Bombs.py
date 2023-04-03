R, C = map(int, input().split())
B = [[c for c in input()] for _ in range(R)]


def get_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


bombs = []
walls = []

for i in range(R):
    for j in range(C):
        if B[i][j] == '#':
            walls.append((i, j))
        elif B[i][j] != '.':
            bombs.append((i, j))


for p1 in bombs:
    power = int(B[p1[0]][p1[1]])
    B[p1[0]][p1[1]] = '.'
    for p2 in walls:
        if get_distance(p1, p2) <= power:
            B[p2[0]][p2[1]] = '.'

for i in range(R):
    print(*B[i], sep='')
