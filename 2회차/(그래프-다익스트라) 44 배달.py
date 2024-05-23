import heapq

def solution(N, road, K):
    startNode= 1

    # 먼저 다익스트라 알고리즘
    que = []
    heapq.heapify(que)
    heapq.heappush(que, [0, startNode])

    distances= [float('inf') for _ in range(N+1)]
    distances[startNode]= 0

    graph = {i: [] for i in range(1, N + 1)}
    for a, b, weight in road:
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    while que:
        d, node= heapq.heappop(que)
        if distances[node] < d:
            continue

        for adj_node, weight in graph[node]:
            if d + weight < distances[adj_node]:
                distances[adj_node]= d + weight
                heapq.heappush(que, [d+weight, adj_node])

    return len([i for i in distances if i<=K])

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2],
                   [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3],
                   [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))