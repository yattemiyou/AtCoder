H = int(input())

count = 0

while H > 0:
    count += 1
    H = H // 2

print(2 ** count - 1)
