N, T = map(int, input().split())

cumsum = [0]

for A in input().split():
    cumsum.append(cumsum[-1] + int(A))

T = T % cumsum[-1]

for i in range(N):
    if cumsum[i] < T < cumsum[i + 1]:
        print(str(i + 1) + ' ' + str(T - cumsum[i]))
        break
