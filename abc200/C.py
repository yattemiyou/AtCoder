from collections import Counter

N = int(input())
counter = Counter(map(lambda s: int(s) % 200, input().split()))

answer = 0

for c in counter.items():
    answer += c[1] * (c[1]-1) // 2

print(answer)
