import heapq
def solution(graph, start):
    # 각 노드가 가져야 할 정보: 최소 비용(직전 노드는 여기서 사용하지 않음)

    # 1. 모든 노드의 최소 거리 값을 무한대로 초기화
    distances= {node: float("inf") for node in graph} # {'A': inf, 'B': inf, 'C': inf}
    # 1-1. 시작 노드의 최소 거리는 0으로
    distances[start]= 0 # {'A': 0, 'B': inf, 'C': inf}

    queue= []
    heapq.heappush(queue, [distances[start], start])
    paths= {start: [start]}

    while queue:
        # heapq를 사용하면 pop할 때 키, 즉 거리가 가장 작은 노드를 pop할 수 있게됨
        current_distance, current_node=heapq.heappop(queue) # current: 현재까지의 최소 비용과 선택된 노드
        if distances[current_node] < current_distance:
            continue

        for adjacent_node, weight in graph[current_node].items(): # b,c
            distance= current_distance + weight
            if distance < distances[adjacent_node]:
                distances[adjacent_node]= distance # 최소 비용 업데이트
                paths[adjacent_node]= paths[current_node] + [adjacent_node]
                heapq.heappush(queue, [distance, adjacent_node])

    sorted_paths= {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]

print(solution({'A': {'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}},'A'))
print(solution({'A': {'B':1}, 'B': {'C':5}, 'C': {'D':1}, 'D': {}},'A'))