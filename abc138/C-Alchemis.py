N = int(input())
v = list(map(int, input().split()))

v.sort()

for i in range(1, N):
    v[i] = (v[i-1] + v[i]) / 2

print(v[i])
