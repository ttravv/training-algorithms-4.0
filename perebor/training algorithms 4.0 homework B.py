def count_ways(N):
    # Функция для проверки, видят ли динозавры друг друга
    def can_place(i, j, placed):
        for x, y in placed:
            if i == x or j == y or abs(i - x) == abs(j - y):
                return False
        return True

    # Функция для рекурсивного перебора всех возможных расстановок
    def backtrack(row, placed):
        nonlocal count
        if row == N:
            count += 1
            return
        for col in range(N):
            if can_place(row, col, placed):
                placed.append((row, col))
                backtrack(row + 1, placed)
                placed.pop()

    count = 0
    backtrack(0, [])
    return count

# Ввод числа N
N = int(input())

# Вывод количества способов расселить динозавров
print(count_ways(N))
