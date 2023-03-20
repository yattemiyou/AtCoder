N = int(input())
A = [a for a in map(int, input().split()) if a % 2 == 0]

print(*A)
