import heapq
def solution(graph, start):
    distance= {node: float('inf') for node in graph}
    distance[start]= 0

    path= {start: [start]}

    que= []
    heapq.heappush(que, [distance[start], start])

    while que:
        d, node= heapq.heappop(que)
        if distance[node] < d:
            continue

        for adj_node, weight in graph[node].items():
            if d + weight < distance[adj_node]:
                distance[adj_node]= d + weight
                path[adj_node]= path[node] + [adj_node]
                heapq.heappush(que, [d + weight, adj_node])

    sorted_path= dict(sorted(path.items()))
    return [distance, sorted_path]

print(solution({'A': {'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}},'A'))
print(solution({'A': {'B':1}, 'B': {'C':5}, 'C': {'D':1}, 'D': {}},'A'))

# 키 값을 기준으로 딕셔너리를 정렬: sorted(path.items())
# 정렬된 결과를 딕셔너리로 변환: dict(sorted(path.items())
# 딕셔너리의 값을 기준으로 정렬: sorted(path.items(), key= lambda item:item[1])
# 나머지 sorted는 python-summary의 Algorithm/Sorting/sort, sorted 함수에  . .