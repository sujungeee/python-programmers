# 교재: heapq, 다익스트라, 그래프(배열)
import heapq

def solution(N, road, K):
    graph= [[] for _ in range(N+1)]
    distances= [float("inf")]*(N+1)
    distances[1]= 0

    # 그래프 구성
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    heap= []
    heapq.heappush(heap, (0, 1)) # 비용, 노드

    while heap:
        cost, node= heapq.heappop(heap)

        for next_node, next_cost in graph[node]:
            dist= cost + next_cost
            if dist < distances[next_node]:
                distances[next_node]= dist
                heapq.heappush(heap, (dist, next_node))

    return len([i for i in distances if i<=K])

print(solution(5, [[1,2,1], [2,3,3], [5,2,2], [4,1,2], [5,3,1], [5,4,2]],3))
print(solution(6,[[1,2,1], [1,3,2], [2,3,2], [3,4,3], [3,5,2], [3,5,3], [5,6,1]], 4))