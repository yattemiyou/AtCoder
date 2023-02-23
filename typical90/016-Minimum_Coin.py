N = int(input())
A, B, C = sorted(map(int, input().split()), reverse=True)


def solve():
    coin = 9999

    for i in range(N // A, -1, -1):
        max = coin
        for j in range(max - i, -1, -1):
            amount = A * i + B * j
            if amount > N:
                continue

            if (N - amount) % C == 0:
                coin = min(coin, i + j + (N - amount) // C)

    return coin


print(solve())
