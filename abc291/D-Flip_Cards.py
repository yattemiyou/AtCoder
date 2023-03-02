MOD = 998244353

N = int(input())
card = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
    for prev in range(2):
        for cur in range(2):
            if card[i-1][prev] != card[i][cur]:
                dp[i][cur] += dp[i-1][prev]
    dp[i][0] %= MOD
    dp[i][1] %= MOD

print((dp[N-1][0] + dp[N-1][1]) % MOD)
