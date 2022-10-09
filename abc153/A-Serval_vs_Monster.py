H, A = map(int, input().split())

n = H // A

if H % A == 0:
    print(n)
else:
    print(n + 1)
