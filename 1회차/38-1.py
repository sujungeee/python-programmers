# 깊이 우선 탐색 by 스택
from collections import defaultdict
def solution(graph, start):
    adj_list= defaultdict(list)
    for u, v in graph: # u 노드로부터 갈 수 있는 v들을 값으로 한 딕셔너리를 생성
        adj_list[u].append(v)

    def dfs(node, visited, result):
        stack= [node]
        while stack:
            vNode= stack.pop()
            if vNode in visited:
                continue
            else:
                visited.add(vNode)
                result.append(vNode) # 방문한 노드는 탐색이 완료된 노드
                adj_node= adj_list[vNode]
                for i in range(len(adj_node)-1, -1,-1):
                    stack.append(adj_node[i])
        return result

    visited= set()
    result= [] # 깊이 우선 탐색의 경로
    dfs(start, visited, result)

    return result

print(solution([['A','B'], ['B', 'C'], ['C', 'D'], ['D', 'E']],'A'))
print(solution([['A','B'], ['A', 'C'], ['B','D'], ['B','E'], ['C','F'], ['E','F']],'A'))