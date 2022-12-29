N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))

    command = query[0]
    k = query[1]

    if command == 1:
        A[k-1] = query[2]
    else:
        print(A[k-1])
