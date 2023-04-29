import math


def get_prime_list(n):
    answer = []

    prime_table = [True] * (n + 1)
    prime_table[0] = False
    prime_table[1] = False

    for i in range(2, len(prime_table)):
        if prime_table[i]:
            answer.append(i)
            for j in range(2*i, len(prime_table), i):
                prime_table[j] = False

    return answer


N = int(input())
primes = get_prime_list(int(math.sqrt(N/12)))

answer = 0

for i in range(len(primes)-2):
    a = primes[i]

    for j in range(i+1, len(primes)-1):
        b = primes[j]

        if a**2 * b * primes[j+1]**2 > N:
            break

        for k in range(j+1, len(primes)):
            c = primes[k]

            if a**2 * b * c**2 > N:
                break

            answer += 1

print(answer)
