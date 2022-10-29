def f(x, cache):
    if x == 0:
        return 1

    if not x in cache:
        cache[x] = f(int(x/2), cache) + f(int(x/3), cache)

    return cache[x]


N = int(input())

print(f(N, {}))
