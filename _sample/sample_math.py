from collections import Counter


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


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


def count_factors(n):
    answer = 1
    for c in Counter(factorize_prime(n)):
        answer *= c[1]+1

    return answer


def get_factors(n):
    answer = []

    for i in range(1, n):
        if i * i > n:
            break

        if n % i != 0:
            continue

        answer.append(i)

        if i != n//i:
            answer.append(n//i)

    return sorted(answer)

# （参考）
# https://math.nakaken88.com/textbook/cp-binary-exponentiation-and-recursive-function/


def modpow(base, exp, mod):
    if exp == 0:
        return 1

    if exp == 1:
        return base % mod

    if exp % 2 == 1:
        return base * modpow(base, exp-1, mod) % mod

    tmp = modpow(base, exp // 2, mod)

    return (tmp * tmp) % mod
