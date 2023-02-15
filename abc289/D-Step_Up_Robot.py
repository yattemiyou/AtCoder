N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = set(map(int, input().split()))

X = int(input())

dp = [True] + [False] * X

for i in range(1, X + 1):
    if i in B:
        continue

    for a in A:
        if i - a >= 0:
            dp[i] |= dp[i - a]

print('Yes' if dp[X] else 'No')
