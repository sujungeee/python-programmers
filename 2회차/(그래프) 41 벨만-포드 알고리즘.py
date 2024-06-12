def solution(graph, source):
    # 그래프의 노드 수
    num_vertices= len(graph)

    # 거리 배열 초기화
    distance= [float('inf') for _ in range(num_vertices)]
    distance[source]= 0

    # 직전 노드 배열
    prodecessor= [None for _ in range(num_vertices)]

    # 최단 경로 갱신
    for _ in range(num_vertices-1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distance[u]+weight < distance[v]:
                    distance[v]= distance[u]+weight
                    prodecessor[v]= u

    # 음의 가중치 순회 체크
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u]+weight < distance[v]:
                return [-1]

    return [distance, prodecessor]

print(solution([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0))
print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))