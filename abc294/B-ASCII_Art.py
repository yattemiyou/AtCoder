def to_ascii(x):
    n = int(x)
    return chr(ord('A') + (n - 1)) if n != 0 else '.'


H, W = map(int, input().split())
A = [list(map(to_ascii, input().split())) for _ in range(H)]

for raw in A:
    print(*raw, sep='')
