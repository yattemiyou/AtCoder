def dfs(n, x):
    if n == 0:
        return 1

    if x == 1:
        return 0
    elif x <= burger[n - 1] + 1:
        return dfs(n - 1, x - 1)
    elif x == 1 + burger[n - 1] + 1:
        return 1 + patty[n - 1]
    else:
        return dfs(n - 1, x - (1 + burger[n - 1] + 1)) + 1 + patty[n - 1]


N, X = map(int, input().split())

patty = [1]
burger = [1]

for i in range(1, N + 1):
    patty.append((patty[i - 1] * 2) + 1)
    burger.append((burger[i - 1] * 2) + 3)

print(dfs(N, X))
