import sys

# Функция для нахождения кратчайшего пути с помощью алгоритма Дейкстры
def shortest_path(graph, start, end):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0
    parent = [-1] * n

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
                parent[i] = min_index

    # Восстановление пути
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    return path[::-1] if distance[end] != sys.maxsize else []

# Чтение ввода
N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# Вызов функции для нахождения кратчайшего пути
result = shortest_path(graph, S - 1, F - 1)

# Вывод результата
if result:
    print(*[v + 1 for v in result])
else:
    print(-1)
