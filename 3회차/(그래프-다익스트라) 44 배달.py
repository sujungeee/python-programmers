import heapq
def solution(N, road, K):
    distances= [float('inf') for _ in range(N+1)]
    distances[1]= 0

    graph= {i:[] for i in range(1, N+1)}
    for r in road:
        graph[r[0]].append([r[2], r[1]])
        graph[r[1]].append([r[2], r[0]])

    que= []
    heapq.heappush(que, [0, 1])
    while que:
        d, node= heapq.heappop(que)
        if distances[node] < d:
            continue

        for weight, adj_node in graph[node]:
            if distances[node] + weight < distances[adj_node]:
                distances[adj_node]= distances[node]+ weight
                heapq.heappush(que, [distances[adj_node], adj_node])

    return len([i for i in distances if i<=K])

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]] ,4))