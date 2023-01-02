# PyPy3で提出しないとダメだった。
# （参考）https://qiita.com/y-oksaku/items/f0c5c4681bc30dddf7f4
N, P, Q = map(int, input().split())

A = list(map(int, input().split()))

answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    if A[i] % P * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q:
                        answer += 1
print(answer)
