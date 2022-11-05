N, M = map(int, input().split())

city = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())

    city[A - 1].append(B)
    city[B - 1].append(A)

for road in city:
    print(len(road), *sorted(road))
