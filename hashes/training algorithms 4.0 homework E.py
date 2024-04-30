def count_palindromic_substrings(s):
    n = len(s)
    count = 0

    # Преобразование строки s для вставки специальных символов между символами
    modified_s = '#' + '#'.join(s) + '#'

    # Массив для хранения длин палиндромов с центром в каждой позиции
    lengths = [0] * len(modified_s)
    center = 0  # Центр самого правого палиндрома
    right = 0   # Правая граница самого правого палиндрома

    for i in range(1, len(modified_s) - 1):
        # Определяем начальное значение длины палиндрома
        if i < right:
            lengths[i] = min(right - i, lengths[2 * center - i])

        # Попытка расширить палиндром в обе стороны
        while i - lengths[i] - 1 >= 0 and i + lengths[i] + 1 < len(modified_s) and \
                modified_s[i - lengths[i] - 1] == modified_s[i + lengths[i] + 1]:
            lengths[i] += 1

        # Если палиндром стал длиннее, обновляем центр и границы
        if i + lengths[i] > right:
            center = i
            right = i + lengths[i]

        # Каждый найденный палиндром прибавляется к общему количеству
        count += (lengths[i] + 1) // 2

    return count

# Ввод строки
s = input()

# Подсчет палиндромов и вывод результата
print(count_palindromic_substrings(s))
