def dfs(number, flags):
    if number > N:
        return 0

    sum = 0

    if 1 <= number <= N and flags == 0b111:
        sum += 1

    sum += dfs(number * 10 + 3, flags | 0b001)
    sum += dfs(number * 10 + 5, flags | 0b010)
    sum += dfs(number * 10 + 7, flags | 0b100)

    return sum


N = int(input())

print(dfs(0, 0))
