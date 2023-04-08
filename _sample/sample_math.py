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

