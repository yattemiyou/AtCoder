import math

def lcm(a, b):
    return  a * int(b / math.gcd(a, b))

n = int(input())

x = 1

for i in range(2, n+1):
    x = lcm(x, i)

print(x + 1)
