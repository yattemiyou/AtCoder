A, B, W = map(int, input().split())
W *= 1000

# A*N <= W*1000 <= B*Nの場合に成立

# 切り上げ
min = int((W + B - 1) / B)
# 切り捨て
max = int(W / A)

if min <= max:
    print(min, max)
else:
    print('UNSATISFIABLE')
