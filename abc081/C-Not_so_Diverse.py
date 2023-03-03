from collections import defaultdict

N, K = map(int, input().split())

ball = defaultdict(int)

for A in input().split():
    ball[A] += 1

if len(ball) - K > 0:
    print(sum(sorted(ball.values())[0:len(ball)-K]))
else:
    print('0')
