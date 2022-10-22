def to_decimal(value, base):
    d = 0

    for i in range(len(value)):
        d += base ** i * int(value[len(value) - 1 - i])

    return d


K = int(input())
A, B = input().split()

print(to_decimal(A, K) * to_decimal(B, K))
