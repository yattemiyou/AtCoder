N, M = map(int, input().split())

C = []
for _ in range(M):
    input()
    C.append(set(map(int, input().split())))

answer = 0

for i in range(1, 2**M):
    bits = bin(i)[2:].zfill(M)

    s = set()

    for j in range(M):
        if bits[j] == '1':
            s = s | C[j]
            if len(s) == N:
                answer += 1
                break
print(answer)
