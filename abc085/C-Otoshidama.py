N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1 - i):
        k = N - (i + j)
        sum = 10000 * i + 5000 * j + 1000 * k
        if sum == Y:
            print(str(i) + ' ' + str(j) + ' ' + str(k))
            break
    else:
        continue
    break
else:
    print('-1 -1 -1')
