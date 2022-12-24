from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = deque()

for i in range(n):
    if i % 2 == len(a) % 2:
        b.append(a[i])
    else:
        b.appendleft(a[i])

print(*b)
