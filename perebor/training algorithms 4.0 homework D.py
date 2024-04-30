import sys

def hungarian(graph, N):
    INF = sys.maxsize
    
    def dfs(u, visited, path, weight):
        nonlocal min_weight
        if len(path) == N:
            min_weight = min(min_weight, weight + graph[u][0])  # Добавляем вес ребра обратно к вершине 1
            return
        for v in range(N):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                dfs(v, visited, path + [v], weight + graph[u][v])
                visited[v] = False

    min_weight = INF
    visited = [False] * N
    visited[0] = True  # Начинаем с вершины 1
    dfs(0, visited, [0], 0)
    
    return min_weight if min_weight != INF else -1

# Ввод данных
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# Нахождение минимальной суммарной длины цикла
result = hungarian(graph, N)
print(result)
