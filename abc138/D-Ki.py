from collections import defaultdict, deque

N, Q = map(int, input().split())

graph = defaultdict(lambda: [])
counter = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p] += x

targets = deque()
targets.append(1)

visited = {1}

while targets:
    parent = targets.popleft()

    for child in graph[parent]:
        if not child in visited:
            targets.append(child)
            visited.add(child)

            counter[child] += counter[parent]

print(*counter[1:])
