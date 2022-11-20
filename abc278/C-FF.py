from collections import defaultdict

N, Q = map(int, input().split())

graph = defaultdict(set)

for i in range(Q):
    T, A, B = map(int, input().split())

    if T == 1:
        graph[A].add(B)
    if T == 2:
        if B in graph[A]:
            graph[A].remove(B)
    if T == 3:
        if B in graph[A] and A in graph[B]:
            print('Yes')
        else:
            print('No')
