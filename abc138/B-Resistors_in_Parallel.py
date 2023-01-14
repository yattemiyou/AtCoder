N = int(input())
A = list(map(int, input().split()))

sum = 0.0

for a in A:
    sum += 1/a

print(1/sum)
