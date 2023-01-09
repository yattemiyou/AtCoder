from collections import defaultdict

#
N = int(input())
print(N)

#
N, M = map(int, input().split())
print(N, M)

#
A = list(map(int, input().split()))

#
S = [input() for _ in range(N)]
print(S)

#
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)

#
N = int(input())

graph = defaultdict(lambda: list())

for _ in range(N):
    A, B = map(int, input().split())

    graph[A].append(B)
    graph[B].append(A)
print(graph)
