N = int(input())

t0, x0, y0 = 0, 0, 0

for i in range(N):
    t1, x1, y1 = map(int, input().split())

    time = t1 - t0
    distance = abs(x1 - x0) + abs(y1 - y0)

    if time < distance or (time - distance) % 2 == 1:
        print('No')
        break

    t0, x0, y0 = t1, x1, y1
else:
    print('Yes')
