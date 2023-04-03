N = int(input())
A = list(map(int, input().split()))

answer = 0
socks = set()

for a in A:
    if a in socks:
        answer += 1
        socks.remove(a)
    else:
        socks.add(a)

print(answer)
