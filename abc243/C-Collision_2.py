from collections import defaultdict

N = int(input())

persons = defaultdict(list)

for i in range(N):
    X, Y = map(int, input().split())
    persons[Y].append((X, i))

S = input()


def solve():
    for y in persons.keys():
        flag = False
        for p in sorted(persons[y]):
            if flag and S[p[1]] == 'L':
                return 'Yes'
            if S[p[1]] == 'R':
                flag = True
    return 'No'


print(solve())
