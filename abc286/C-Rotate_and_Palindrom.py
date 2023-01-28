import math

N, A, B = map(int, input().split())
S = input()

answer = math.inf

for i in range(N):
    cost = A * i
    s = S[i:] + S[0:i]

    for j in range(N // 2):
        if s[j] == s[N-j-1]:
            continue
        cost += B

    answer = min(cost, answer)

print(answer)
