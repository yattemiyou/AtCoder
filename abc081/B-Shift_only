N = int(input())
A = list(map(int, input().split()))

count = 0
is_exist_odd = False

while True:
    for i in range(N):
        if A[i] % 2 != 0:
            is_exist_odd = True
            break

        A[i] = A[i] / 2

    if is_exist_odd:
        break

    count = count + 1

print(count)
