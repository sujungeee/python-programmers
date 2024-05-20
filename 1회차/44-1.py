# heapq, 다익스트라, 딕셔너리
import heapq

def solution(N, road, K):
    # 거리
    distances= [float("inf")]*(N+1)
    distances[1]= 0
    # heapq
    heap= []
    heapq.heappush(heap, (0, 1)) # 비용, 노드

    # 딕셔너리
    dic= {i: [] for i in range(1,N+1)}
    for a,b, weight in road:
        dic[a].append((b, weight))
        dic[b].append((a, weight))

    while heap:
        distance, node= heapq.heappop(heap)

        for ad_node, weight in dic[node]:
            dist= distance+ weight
            if dist < distances[ad_node]:
                distances[ad_node]= dist
                heapq.heappush(heap, (dist, ad_node))

    return len([i for i in distances if i<=K])

print(solution(5, [[1,2,1], [2,3,3], [5,2,2], [4,1,2], [5,3,1], [5,4,2]],3))
print(solution(6,[[1,2,1], [1,3,2], [2,3,2], [3,4,3], [3,5,2], [3,5,3], [5,6,1]], 4))