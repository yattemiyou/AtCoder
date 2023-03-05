from collections import Counter

N = int(input())

prev = Counter(input())

for _ in range(1, N):
    cur = Counter(input())

    keys = prev.keys() & cur.keys()

    temp = dict()
    for k in keys:
        if prev[k] < cur[k]:
            temp[k] = prev[k]
        else:
            temp[k] = cur[k]
    prev = temp

for k in sorted(prev.keys()):
    print(k * prev[k], end='')
print()
