A, B = map(int, input().split())

for i in range(10):
    answer = B * 10 + i

    if int(answer * 0.08) == A:
        print(answer)
        break
else:
    print(-1)
