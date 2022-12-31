N = int(input())
S = list(map(int, input().split()))

print(str(S[0]), end=' ')

for i in range(1, N):
    print(str(S[i] - S[i-1]), end=' ')

print()
