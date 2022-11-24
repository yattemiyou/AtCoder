import bisect

N = int(input())

cumsum = [0]

for A in input().split():
    cumsum.append(cumsum[-1] + int(A))

if cumsum[N] % 10 != 0:
    print('No')
    exit()

for i in range(N):
    target = cumsum[N] // 10

    if cumsum[N] - cumsum[i] < target:
        target = target - (cumsum[N] - cumsum[i])
        i = 0

    index = bisect.bisect_left(cumsum, target + cumsum[i], lo=i+1)

    if cumsum[index] == target + cumsum[i]:
        print('Yes')
        exit()

print('No')
