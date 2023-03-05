N, K = map(int, input().split())
S = input()

for s in S:
    if s == 'o' and K > 0:
        K -= 1
        print(s, end='')
    else:
        print('x', end='')
print()
