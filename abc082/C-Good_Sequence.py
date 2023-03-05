from collections import Counter

N = int(input())
counter = Counter(map(int, input().split()))

answer = 0

for n, count in counter.items():
    if count >= n:
        answer += count - n
    else:
        answer += count

print(answer)
