from collections import defaultdict

S = input()

d = defaultdict(lambda: 0)

for c in S:
    d[c] += 1

print('Yes' if len(d.keys()) == 2 and d[c] == 2 else 'No')
