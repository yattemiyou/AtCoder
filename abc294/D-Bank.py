from sys import stdin
def input(): return stdin.readline()[:-1]


N, Q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(Q)]

person = [0] * N
next = 0
called = 0

for e in event:
    if e[0] == 1:
        person[next] = 1
        next += 1
    elif e[0] == 2:
        person[e[1]-1] = 2
    elif e[0] == 3:
        while person[called] == 2:
            called += 1
        print(called + 1)
