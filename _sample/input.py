from collections import defaultdict

#
N = int(input())
print(N)

#
N, M = map(int, input().split())
print(N, M)

#
N = int(input())

graph = defaultdict(lambda: list())

for _ in range(N):
    A, B = map(int, input().split())

    graph[A].append(B)
    graph[B].append(A)
print(graph)
