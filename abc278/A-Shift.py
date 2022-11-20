N, K = map(int, input().split())
A = list(map(int, input().split()))

if K > N:
    K = N

A = A[K:] + [0] * K

print(*A)
