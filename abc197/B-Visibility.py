H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

X -= 1
Y -= 1

answer = 1 if S[X][Y] == '.' else 0

# 上方向
for i in range(X-1, -1, -1):
    if S[i][Y] == '.':
        answer += 1
    else:
        break

# 下方向
for i in range(X+1, H):
    if S[i][Y] == '.':
        answer += 1
    else:
        break

# 左方向
for i in range(Y-1, -1, -1):
    if S[X][i] == '.':
        answer += 1
    else:
        break

# 右方向
for i in range(Y+1, W):
    if S[X][i] == '.':
        answer += 1
    else:
        break

print(answer)
