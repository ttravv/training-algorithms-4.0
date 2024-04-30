import sys

# Функция для нахождения кратчайшего расстояния между вершинами с помощью алгоритма Дейкстры
def shortest_path(graph, start, end):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    for _ in range(n):
        min_dist = sys.maxsize
        min_index = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True

        for i in range(n):
            if graph[min_index][i] != -1 and distance[min_index] + graph[min_index][i] < distance[i]:
                distance[i] = distance[min_index] + graph[min_index][i]

    return distance[end] if distance[end] != sys.maxsize else -1

# Чтение ввода
N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# Вызов функции для нахождения кратчайшего расстояния
result = shortest_path(graph, S - 1, F - 1)

# Вывод результата
print(result)
