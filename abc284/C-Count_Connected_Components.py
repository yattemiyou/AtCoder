from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(lambda: list())

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph[u].append(v)
    graph[v].append(u)

visited = [0] * N

answer = 0

for i in range(N):
    if visited[i] != 0:
        continue

    answer += 1

    targets = deque()
    targets.append(i)

    visited[i] = answer

    while targets:
        vertex = targets.popleft()

        for v in graph[vertex]:
            if visited[v] == 0:
                targets.append(v)
                visited[v] = answer

print(answer)
