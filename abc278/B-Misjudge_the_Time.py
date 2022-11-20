H, M = input().split()

h = int(H)
m = int(M)

while True:
    if h < 20 and h % 10 < 6:
        break
    elif h >= 20 and (m % 60) < 40:
        break

    m += 1
    h = (int(H) + m // 60) % 24

print(str(h) + ' ' + str(m % 60))
