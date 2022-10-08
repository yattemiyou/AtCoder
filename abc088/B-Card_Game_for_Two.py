N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

if len(A) % 2 == 1:
    A.append(0)

sub = sum([A[i] - A[i + 1] for i in range(0, len(A) - 1, 2)])

print(sub)
