N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda s: A[int(s)-1], input().split()))

print(sum(B))
