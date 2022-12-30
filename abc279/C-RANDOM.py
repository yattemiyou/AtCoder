H, W = map(int, input().split())

S = [list() for _ in range(W)]
T = [list() for _ in range(W)]

for _ in range(H):
    for i, c in enumerate(input()):
        S[i].append(c)

for _ in range(H):
    for i, c in enumerate(input()):
        T[i].append(c)

if sorted(S) == sorted(T):
    print('Yes')
else:
    print('No')
