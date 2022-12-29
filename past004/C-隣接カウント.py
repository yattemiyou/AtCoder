N, M = map(int, input().split())

s = [input() for _ in range(N)]

dx = [0, 1, 1, 0, -1, -1, -1,  0,  1]
dy = [0, 0, 1, 1,  1,  0, -1, -1, -1]

for i in range(N):
    for j in range(M):
        count = 0
        for k in range(9):
            if i+dy[k] < 0 or i+dy[k] >= N:
                continue
            if j+dx[k] < 0 or j+dx[k] >= M:
                continue
            if s[i+dy[k]][j+dx[k]] == '#':
                count += 1
        print(count, end='')
    print()
