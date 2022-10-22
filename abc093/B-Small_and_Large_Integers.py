A, B, K = map(int, input().split())

for i in range(A, min(A+K, B+1)):
    print(i)

for j in range(max(i+1, B-K+1), B+1):
    print(j)
