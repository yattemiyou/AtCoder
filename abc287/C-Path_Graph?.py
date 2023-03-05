from collections import defaultdict

graph = defaultdict(list)

N, M = map(int, input().split())

edge = set(range(1, N+1))

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    if len(graph[u]) > 1 and u in edge:
        edge.remove(u)

    graph[v].append(u)
    if len(graph[v]) > 1 and v in edge:
        edge.remove(v)


def solve():
    if len(edge) != 2:
        return 'No'

    cur = edge.pop()
    path = {cur}

    while len(path) < N:
        next = graph[cur]

        if len(next) != 1:
            return 'No'

        if len(graph[next[0]]) >= 1:
            graph[next[0]].remove(cur)

        cur = next[0]
        if cur in path:
            return 'No'

        path.add(cur)

    return 'Yes'


print(solve())
