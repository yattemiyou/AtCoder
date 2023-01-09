from collections import defaultdict, deque

graph = defaultdict(lambda: list())

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())

    graph[A].append(B)
    graph[B].append(A)

targets = deque()
targets.append(1)

visited = {1}

while targets:
    vertex = targets.popleft()

    for v in graph[vertex]:
        if not v in visited:
            targets.append(v)
            visited.add(v)

print(max(visited))
