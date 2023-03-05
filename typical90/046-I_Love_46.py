from collections import Counter

N = int(input())
A = Counter(map(lambda s: int(s) % 46, input().split()))
B = Counter(map(lambda s: int(s) % 46, input().split()))
C = Counter(map(lambda s: int(s) % 46, input().split()))

answer = 0

for a in A.items():
    for b in B.items():
        for c in C.items():
            if (a[0] + b[0] + c[0]) % 46 == 0:
                answer += a[1] * b[1] * c[1]

print(answer)
