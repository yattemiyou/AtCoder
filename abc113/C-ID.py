from collections import defaultdict

N, M = map(int, input().split())
prefecture = [[] for _ in range(N)]

P_Y = []
for i in range(M):
    P, Y = map(int, input().split())
    P_Y.append((P, Y))

    P -= 1
    prefecture[P].append(Y)

year = defaultdict(lambda: 0)

for p in prefecture:
    p.sort()

    order = 0
    for y in p:
        order += 1
        year[y] = order

for p, y in P_Y:
    print(str(p).zfill(6) + str(year[y]).zfill(6))
