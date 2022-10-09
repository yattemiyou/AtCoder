combination = {}

N, M = map(int, input().split())

for i in range(1, N):
    combination[i] = [j for j in range(i + 1, N + 1)]

for m in range(M):
    k, *x = map(int, input().split())

    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[j] in combination[x[i]]:
                combination[x[i]].remove(x[j])

if all(len(v) == 0 for v in combination.values()):
    print('Yes')
else:
    print('No')
