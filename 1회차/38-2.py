# 깊이 우선 탐색 by 재귀(교재)
from collections import defaultdict

def solution(graph, start):
    adj_list = defaultdict(list) # 인접 리스트
    for u, v in graph:  # u 노드로부터 갈 수 있는 v들을 값으로 한 딕셔너리를 생성
        adj_list[u].append(v)

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in adj_list.get(node, []): # adj_list.get(node, []) 인 이유: 인접한 노드가 없으면 빈 리스트를 넣어준다. in []
            if neighbor not in visited:
                dfs(neighbor, visited, result)
        return result

    visited = set()
    result = []  # 깊이 우선 탐색의 경로
    dfs(start, visited, result)

    return result


print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))