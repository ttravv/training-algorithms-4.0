import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    visited = [False] * n
    distance = [float('inf')] * n
    distance[start] = 0
    pq = [(0, start)]  # очередь с приоритетами: (расстояние, вершина)

    while pq:
        dist, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                heapq.heappush(pq, (distance[v], v))

    return distance[end] if distance[end] != float('inf') else -1

# Чтение ввода
N, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(K):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))
A, B = map(int, input().split())

# Вызов функции для нахождения кратчайшего пути
result = dijkstra(graph, A - 1, B - 1)

# Вывод результата
print(result)
