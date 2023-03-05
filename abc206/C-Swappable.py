from collections import Counter

N = int(input())
counter = Counter(map(int, input().split())).most_common()

answer = N * (N-1) // 2

for c in counter:
    if c[1] == 1:
        break
    answer -= c[1] * (c[1]-1) // 2

print(answer)
