from collections import defaultdict

N, M = map(int, input().split())

S = defaultdict(int)
for _ in range(N):
    S[input()[-3:]] += 1

T = {input() for _ in range(M)}

answer = 0

for s in T:
    answer += S[s]

print(answer)
