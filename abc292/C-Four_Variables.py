from collections import Counter
from functools import lru_cache


def factorize_prime(n):
    answer = []

    for p in range(2, n):
        if p * p > n:
            break

        if n % p != 0:
            continue

        e = 0
        while n % p == 0:
            e += 1
            n //= p

        answer.append((p, e))

    if n != 1:
        answer.append((n, 1))

    return answer


@lru_cache(maxsize=200000)
def count_factors(n):
    answer = 1
    for c in Counter(factorize_prime(n)):
        answer *= c[1]+1

    return answer


N = int(input())

answer = 0

for i in range(1, N):
    answer += count_factors(i) * count_factors(N-i)

print(answer)
