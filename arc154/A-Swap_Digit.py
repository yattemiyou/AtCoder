N = int(input())
A = [c for c in input()]
B = [c for c in input()]

for i in range(N):
    if A[i] > B[i]:
        A[i], B[i] = B[i], A[i]

print(int(''.join(A)) * int(''.join(B)) % 998244353)
