n = 5
r = 3

# forループ版
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            print(i, j, k)


# 再帰呼び出し版
def enumerate_combination(n, r, start=0, combination=[]):
    if r <= 0:
        print(*combination, sep=' ')
        return

    for i in range(start, n):
        combination.append(i)
        enumerate_combination(n, r-1, i+1, combination)
        combination.pop()


enumerate_combination(n, r)
