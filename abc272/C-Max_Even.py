N = int(input())
A = sorted(map(int, input().split()), reverse=True)

max = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        sum = A[i] + A[j]
        if sum <= max:
            break
        if sum % 2 == 0:
            max = sum
if max == 0:
    print('-1')
else:
    print(max)
