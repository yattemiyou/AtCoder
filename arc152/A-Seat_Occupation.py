N, L = map(int, input().split())
A = list(map(int, input().split()))

index = 1

for a in A:
    if index >= L and a == 2:
        print('No')
        break

    index += a + 1
else:
    print('Yes')
