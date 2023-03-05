import bisect
from collections import defaultdict
from sys import stdin
def input(): return stdin.readline()[:-1]


def divide_character(s):
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    return d


def find_character(d, c, start):
    if c not in d:
        return -1
    index = bisect.bisect_left(d[c], start)
    return d[c][index] if index < len(d[c]) else -1


def rfind_character(d, c, start):
    if c not in d:
        return -1
    index = bisect.bisect_left(d[c], start)
    return d[c][index-1] if index > 0 else -1


A = divide_character(input())
B = divide_character(input())
Q = int(input())


def solve(S):
    a, b = 0, 0
    head, tail = 0, 10**5

    for i in range(len(S)):
        if head >= 0:
            head = find_character(A, S[i], head)
            if head >= 0:
                a += 1
                head += 1

        if a >= 1 and b >= 1 and a + b == len(S):
            return abs(a - b)

        if tail >= 0:
            tail = rfind_character(B, S[-1-i], tail)
            if tail >= 0:
                b += 1

        if a >= 1 and b >= 1 and a + b == len(S):
            return abs(a - b)
    else:
        return -1


for _ in range(Q):
    print(solve(input()))
