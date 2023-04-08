N, Q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(Q)]

player = [0] * N

for e in event:
    c = e[0]
    n = e[1] - 1
    if c == 1:
        player[n] += 1
    elif c == 2:
        player[n] += 2
    else:
        print('Yes' if player[n] >= 2 else 'No')
