H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]


def is_match(s, t):
    for i in range(H):
        for j in range(W):
            if A[(i-s+H) % H][(j-t+W) % W] != B[i][j]:
                return False
    return True


def solve():
    for s in range(H):
        for t in range(W):
            if is_match(s, t):
                return 'Yes'
    return 'No'


print(solve())
