T = int(input())

answer = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    answer.append(sum([i % 2 == 1 for i in A]))

print(*answer, sep='\n')
