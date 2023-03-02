from collections import defaultdict

N = int(input())

s = defaultdict(int)
for _ in range(N):
    s["".join(sorted(input()))] += 1

answer = 0

for n in s.values():
    answer += (n * (n-1)) // 2

print(answer)
