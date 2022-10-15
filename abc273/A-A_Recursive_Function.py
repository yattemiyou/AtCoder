def f(k):
    if k == 0:
        return 1

    return k * f(k - 1)


N = int(input())

print(f(N))
