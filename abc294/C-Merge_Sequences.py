N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = sorted(A + B)

ranking = {c: i + 1 for i, c in enumerate(C)}

for a in A:
    print(ranking[a], end=' ')
print()

for b in B:
    print(ranking[b], end=' ')
print()
