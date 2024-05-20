def solution(graph, source):
    num_vertices= len(graph) # 그래프의 노드 수

    # 노드의 거리를 무한대로 초기화하고, 시작 노드만 거리를 0으로
    distance= [float('inf')] * num_vertices
    distance[source]= 0
    # 직전 경로 배열 초기
    prodecessor= [None] * num_vertices

    # 최단 경로 구하기
    for temp in range(num_vertices-1): # 4번
        for u in range(num_vertices): # 5번(출발 노드)
            for v, weight in graph[u]: # 노드 0번부터 도착노드, 가중치 값을 순차적으로 확인
                if distance[u]+weight < distance[v]:
                    distance[v]= distance[u]+weight
                    prodecessor[v]= u

    # 음의 가중치 순회 체크
    for u in range(num_vertices): # 0~4번
        for v, weight in graph[u]:
            if distance[u]+weight < distance[v]:
                return [-1]
    return [distance, prodecessor]

print(solution([[(1,4),(2,3),(4,-6)], [(3,5)], [(1,2)], [(0,7), (2,4)], [(2,2)]], 0))
print(solution([[(1,5),(2,-1)], [(2,2)], [(3,-2)], [(0,2),(1,6)]], 0))