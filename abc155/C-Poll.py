from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S).most_common()

max = counter[0][1]

name = []

for c in counter:
    if c[1] < max:
        break
    name.append(c[0])

print(*sorted(name), sep='\n')
