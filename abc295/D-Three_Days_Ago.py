from collections import defaultdict

S = input()

count = defaultdict(int)

cumsum = [0] * 10
count['0'*10] += 1

for c in S:
    n = int(c)
    cumsum[n] = (cumsum[n] + 1) % 2
    count[''.join(map(str, cumsum))] += 1

answer = 0

for v in count.values():
    if v > 1:
        answer += (v * (v-1)) // 2

print(answer)
