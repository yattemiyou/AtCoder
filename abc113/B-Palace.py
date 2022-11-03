N = int(input())
T, A = map(int, input().split())
H = list(map(lambda x: abs((T - A) - int(x) * 0.006), input().split()))

print(min(enumerate(H), key=lambda x: x[1])[0] + 1)
