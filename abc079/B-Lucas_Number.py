N = int(input())

prev2 = 2
prev1 = 1

if N == 1:
    print(1)
else:
    for i in range(2, N+1):
        L = prev2 + prev1

        prev2 = prev1
        prev1 = L
    print(L)
