H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

route = set()
answer = 0


def solve(i, j):
    global route
    global answer

    if i == H-1 and j == W-1:
        answer += 1
        return

    if i + 1 < H and not A[i+1][j] in route:
        route.add(A[i+1][j])
        solve(i+1, j)
        route.remove(A[i+1][j])

    if j + 1 < W and not A[i][j+1] in route:
        route.add(A[i][j+1])
        solve(i, j+1)
        route.remove(A[i][j+1])

    return answer


route.add(A[0][0])
print(solve(0, 0))
