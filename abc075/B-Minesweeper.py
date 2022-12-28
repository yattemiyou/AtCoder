difference = [
    (1, 0), (1, 1), (0, 1), (-1, 1),
    (-1, 0), (-1, -1), (0, -1), (1, -1)
]

H, W = map(int, input().split())

S = []

for _ in range(H):
    row = []
    for c in input():
        if c != '#':
            c = 0
        row.append(c)
    S.append(row)

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue

        for k in range(len(difference)):
            if i + difference[k][0] < 0 or i + difference[k][0] >= H:
                continue
            if j + difference[k][1] < 0 or j + difference[k][1] >= W:
                continue
            if S[i + difference[k][0]][j + difference[k][1]] != '#':
                continue
            S[i][j] += 1

for row in S:
    print(*row, sep='')
