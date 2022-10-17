X = int(input())

answer = 0
money = 100

while money < X:
    answer += 1
    money += money // 100

print(answer)
